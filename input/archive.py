from zipfile import ZipFile
from tqdm import tqdm
import re

from input.read_nyu import read_pgm, read_ppm


class RawDatasetArchive:
    """Loads a zip file containing (a part of) the raw dataset and
    provides member functions for further data processing.
    """

    def __init__(self, zip_path):

        self.zip_path = zip_path
        self.zip = ZipFile(zip_path)
        self.frames = synchronise_frames(self.zip.namelist())
        self.damage_frames = []
        # self.check_frames_integrity()

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, idx):
        return self.frames[idx]

    def check_frames_integrity(self):
        """Prova ad aprire il frame, se si fallisce allora
        allora tale immagine è cosiderata corrotta e dunque verrà esclusa
        dalla lista dei frames.
        TODO
        """
        for frame in tqdm(self.frames, desc=f'Check frames integrity for {self.zip_path}'):
            depth_path, rgb_path = frame
            try:
                with open(depth_path, 'rb') as f:
                    read_pgm(f)
                with open(rgb_path, 'rb') as f:
                    read_ppm(f)
            except Exception:
                print(f'{frame} è corrotto...')
                self.damage_frames.append(frame)

    def frame(self, frame, path=None):
        """
        Extracts a synchronised frame of depth and color images.
        The frame parameter must be a pair of depth and color maps from
        the archive. Optionally the path of an extraction directory can be given.
        """

        return map(lambda name: self.zip.extract(name, path=path), frame)


def synchronise_frames(frame_names):
    """
    Constructs a list of synchronised depth and RGB frames.
    Returns a list of pairs, where the first is the path of a depth image,
    and the second is the path of a color image.
    """

    # Regular expressions for matching depth and color images
    depth_img_prog = re.compile(r'.+/d-.+\.pgm')
    color_img_prog = re.compile(r'.+/r-.+\.ppm')

    # Applies a regex program to the list of names
    def match_names(prog):
        return map(prog.match, frame_names)

    # Filters out Nones from an iterator
    def filter_none(iter):
        return filter(None.__ne__, iter)

    # Converts regex matches to strings
    def match_to_str(matches):
        return map(lambda match: match.group(0), matches)

    # Retrieves the list of image names matching a certain regex program
    def image_names(prog):
        return list(match_to_str(filter_none(match_names(prog))))

    depth_img_names = image_names(depth_img_prog)
    color_img_names = image_names(color_img_prog)

    # By sorting the image names we ensure images come in chronological order
    depth_img_names.sort()
    color_img_names.sort()

    def name_to_timestamp(name):
        """
        Extracts the timestamp of a RGB / depth image from its name.
        """
        _, time, _ = name.split('-')
        return float(time)

    def get_scene_name(name):
        scene, _ = name.split('/')
        return scene

    frames = []
    scene_2_frame_count = dict()
    last_scene = None

    for depth_img_name in depth_img_names:

        depth_time = name_to_timestamp(depth_img_name)
        depth_scene = get_scene_name(depth_img_name)

        if scene_2_frame_count.get(depth_scene, None) is None:
            scene_2_frame_count[depth_scene] = 0

        diff = 99999
        color_with_min = None

        # Keep going through the color images until we find
        # the one with the closest timestamp
        for color_img_name in color_img_names:
            color_time = name_to_timestamp(color_img_name)
            color_scene = get_scene_name(color_img_name)

            new_diff = abs(depth_time - color_time)

            # Moving forward would only result in worse timestamps
            if depth_scene != color_scene:
                break

            if new_diff < diff:
                color_with_min = color_img_name
                diff = new_diff

        scene_2_frame_count[depth_scene] += 1

        if color_with_min is not None:
            frames.append((depth_img_name, color_with_min, str(scene_2_frame_count[depth_scene])))

    return frames
