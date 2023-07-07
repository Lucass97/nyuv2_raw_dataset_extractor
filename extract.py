import argparse

from extractor import NyuV2RawExtractor
from misc.logger import CustomLogger

logger = CustomLogger('NyuV2 Toolbox')


def get_args():
    """
    Parses command line arguments.

    :return: Parsed command line arguments.
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="NyuV2 - Raw Dataset Extractor")
    parser.add_argument("--path", type=str, default="data/raw/basement.zip",
                        help="Relative path to the raw dataset archive file (ZIP format)")
    parser.add_argument("--output_dir", type=str, default="data/extracted", help="Output directory")
    parser.add_argument("--undistort", action="store_true", help="Undistort RGB and depth images", default=True)
    parser.add_argument("--save-undistort-diff", action="store_true",
                        help="Save the difference between the original and undistorted images", default=False)
    parser.add_argument("--fill-depth", action="store_true", help="Use fill depth colorization algorithm",
                        default=False)

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    extractor = NyuV2RawExtractor(path=args.path, output_dir=args.output_dir,
                                  undistort=args.undistort, save_undistort_diff=args.save_undistort_diff,
                                  fill_depth=args.fill_depth)
    extractor.extract()
