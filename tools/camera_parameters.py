import numpy as np

"""
camera_parameters.m
"""

# RGB camera intrinsic matrix
rgb_K_matrix = np.array([[5.1885790117450188e+02, 0, 3.2558244941119034e+02],
                         [0, 5.1946961112127485e+02, 2.5373616633400465e+02],
                         [0, 0, 1]], dtype=np.float32)

# Depth camera intrinsic matrix
depth_K_matrix = np.array([[5.8262448167737955e+02, 0, 3.1304475870804731e+02],
                           [0, 5.8269103270988637e+02, 2.3844389626620386e+02],
                           [0, 0, 1]], dtype=np.float32)

# Depth camera distortion coefficients
depth_distortion_matrix = np.array(
    [-9.9897236553084481e-02, 3.9065324602765344e-01, 1.9290592870229277e-03, -1.9422022475975055e-03,
     -5.1031725053400578e-01], dtype=np.float32)

# RGB camera distortion coefficients
rgb_distortion_matrix = np.array(
    [2.0796615318809061e-01, -5.8613825163911781e-01, 7.2231363135888329e-04, 1.0479627195765181e-03,
     4.9856986684705107e-01], dtype=np.float32)