import cv2
import numpy as np
from skimage.metrics import structural_similarity

from tools.camera_parameters import rgb_K_matrix, depth_K_matrix, rgb_distortion_matrix, depth_distortion_matrix


def undistort_sample(color, depth):
    """
    Undistorts a sample consisting of color and depth images.

    :param color: The color image.
    :type color: numpy.ndarray
    :param depth: The depth image.
    :type depth: numpy.ndarray
    :return: A dictionary containing the undistorted color and depth images,
            as well as the differences between the original and undistorted images.
    :rtype: dict
    """

    rgb = np.asarray(color, dtype=np.float32)
    depth = np.asarray(depth, dtype=np.float32)

    width, height = rgb.shape[1], rgb.shape[0]

    newcameramtx, _ = cv2.getOptimalNewCameraMatrix(rgb_K_matrix, rgb_distortion_matrix,
                                                    (width, height), 1, (width, height))
    undistorted_rgb = cv2.undistort(rgb, rgb_K_matrix, rgb_distortion_matrix, None, newcameramtx)

    newcameramtx, _ = cv2.getOptimalNewCameraMatrix(depth_K_matrix, depth_distortion_matrix,
                                                    (width, height), 1, (width, height))
    undistorted_depth = cv2.undistort(depth, depth_K_matrix, depth_distortion_matrix, None, newcameramtx)

    (score_depth, diff_depth) = structural_similarity(depth, undistorted_depth, full=True, win_size=3,
                                                      data_range=depth.max() - depth.min())
    (score_rgb, diff_rgb) = structural_similarity(rgb, undistorted_rgb, full=True, win_size=3, channel_axis=2,
                                                  data_range=rgb.max() - rgb.min())

    return {
        'color': undistorted_rgb,
        'depth': undistorted_depth,
        'diff_color': diff_rgb,
        'diff_depth': diff_depth
    }
