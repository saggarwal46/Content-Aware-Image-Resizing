import numpy as np
import math


def energy_image(im):

    """ Computes the energy at each pixel using the magnitude of the x and y
    gradients.

    Args:
        im (ndarray): Input image (size: MxNx3, type:uint8).

    Returns:
        ndarray: Energies of all pixels (size: MxNx3, type:double).

    """
    
    rows, columns, channels = im.shape
    energy_im = np.zeros((rows, columns), dtype='float64')
    im = np.dot(im[...,:3], [0.299, 0.587, 0.114])
    a = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    nd_a = np.array(a)
    b = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    nd_b = np.array(b)
    xgradient = np.gradient(im, axis=0)
    ygradient = np.gradient(im, axis=1)
    for i in range(rows):
        for j in range(columns):
            energy_im[i][j] = abs(xgradient[i][j]) + abs(ygradient[i][j])
    return energy_im
