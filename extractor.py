import os
import shutil

import cv2
import numpy as np
from tabulate import tabulate
from tqdm import tqdm

from input.archive import RawDatasetArchive
from input.read_nyu import load_depth_image, load_color_image
from misc.logger import CustomLogger
from tools.depth_conversion import depth_rel_to_depth_abs
from tools.fill_depth_colorization import fill_depth_colorization
from tools.undistort import undistort_sample


class NyuV2RawExtractor:
    """
    NyuV2 - Raw Dataset Extractor

    This class extracts color and depth images from a NyuV2 raw dataset archive.

    Args:
        path (str): Relative path to the raw dataset archive file (ZIP format).
        output_dir (str): Output directory to save the extracted images.
        undistort (bool): Flag to enable undistortion of RGB and depth images.
        save_undistort_diff (bool): Flag to save the difference between the original and undistorted images.
        fill_depth (bool): Flag to use the fill depth colorization algorithm.
    """

    def __init__(self, path: str, output_dir: str, undistort: bool, save_undistort_diff: bool, fill_depth: bool):
        self.logger = CustomLogger("NyuV2 - Raw Dataset Extractor")
        self.path = path
        self.output_dir = output_dir
        self.undistort = undistort
        self.save_undistort_diff = save_undistort_diff
        self.fill_depth = fill_depth

        self.print_parameters()

    def extract(self) -> None:
        """
        Extracts color and depth images from the NyuV2 raw dataset archive.

        The extracted images are saved in the specified output directory.
        Undistortion and fill depth colorization can be applied based on the configuration.
        """

        temp_path = os.path.join(os.path.dirname(self.path), 'temp')
        os.makedirs(temp_path, exist_ok=True)

        dataset_archive = RawDatasetArchive(zip_path=self.path)
        archive_name = os.path.splitext(os.path.basename(self.path))[0]

        self.logger.info(msg=f"{archive_name} - Extracting...")

        pbar = tqdm(total=len(dataset_archive), bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')

        for frame in dataset_archive:

            depth_path, color_path = frame[0], frame[1]

            pbar.set_description(f"Current RGB: {color_path}")

            try:
                # Extract images
                dataset_archive.zip.extract(member=color_path, path=temp_path)
                dataset_archive.zip.extract(member=depth_path, path=temp_path)

                # Read images
                color = load_color_image(os.path.join(temp_path, color_path))
                depth = load_depth_image(os.path.join(temp_path, depth_path))
            except Exception as e:
                self.logger.error(f"{archive_name} - An error occurred while processing the images: {str(e)}")
                continue

            color = np.asarray(color, dtype=np.float32)
            depth = depth_rel_to_depth_abs(np.asarray(depth, dtype=np.float32))

            if self.undistort:
                undistort_results = undistort_sample(color=color, depth=depth)

                color = undistort_results['color']
                depth = undistort_results['depth']
                diff_color = undistort_results['diff_color']
                diff_depth = undistort_results['diff_depth']

            if self.fill_depth:
                depth, _ = fill_depth_colorization(imgRgb=color, imgDepthInput=depth)

            """ Save RGB """

            color_output_path = os.path.join(self.output_dir, color_path[:-4] + '.png')
            color_output_dir = os.path.dirname(color_output_path)
            os.makedirs(color_output_dir, exist_ok=True)

            cv2.imwrite(color_output_path, color)

            """ Save depth map """

            dense_depth_output_path = os.path.join(self.output_dir, depth_path[:-4] + '.png')
            dense_depth_output_dir = os.path.dirname(dense_depth_output_path)
            os.makedirs(dense_depth_output_dir, exist_ok=True)

            cv2.imwrite(dense_depth_output_path, depth * 255 / 10)

            """ Save undistort difference """

            if self.undistort and self.save_undistort_diff:
                diff_color_output_path = os.path.join(self.output_dir, color_path[:-4] + '-diff-undistort.png')
                diff_color_output_dir = os.path.dirname(diff_color_output_path)
                os.makedirs(diff_color_output_dir, exist_ok=True)

                cv2.imwrite(diff_color_output_path, diff_color)

                diff_depth_output_path = os.path.join(self.output_dir, depth_path[:-4] + '-diff-undistort.png')
                diff_depth_output_dir = os.path.dirname(diff_depth_output_path)
                os.makedirs(diff_depth_output_dir, exist_ok=True)

                cv2.imwrite(diff_depth_output_path, diff_depth)

            pbar.update(1)

        pbar.close()

        self.logger.info(msg=f"{archive_name} - Extraction completed")

        txt_path = os.path.join(self.output_dir, archive_name + '.txt')

        self.logger.info(msg=f"{archive_name} - Writing {txt_path} file...")

        with open(txt_path, mode="w") as f:
            for depth_path, color_path, seq_number in dataset_archive.frames:
                color_path = color_path[:-4] + '.png'
                depth_path = depth_path[:-4] + '.png'
                f.write(depth_path + ' ' + color_path + ' ' + seq_number + '\n')

        # Remove temp folder
        shutil.rmtree(temp_path)

        self.logger.info(msg=f"{archive_name} - Task completed")

    def print_parameters(self):
        """
        Prints the initialization parameters in a tabular format using the logger.
        """
        table_data = [
            ["Parameter", "Value"],
            ["Path", self.path],
            ["Output Directory", self.output_dir],
            ["Undistort", self.undistort],
            ["Save Undistort Difference", self.save_undistort_diff],
            ["Fill Depth", self.fill_depth]
        ]

        table = tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")
        self.logger.info(f"Initialization parameters:\n{table}")