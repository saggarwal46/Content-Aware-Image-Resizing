import numpy as np
import cumulative_minimum_energy_map as cm
import find_optimal_vertical_seam as vs
import displaySeam as dS

def reduceWidth(im, energyImage):

    """ Reduces the width of the input image and the energy image by one pixel.

    Args:
        im (ndarray): Image too be reduced (size: MxNx3, type:uint8).
        energyImage (ndarray): 2D matrix containing energies of each pixel
            (size: MxN, type:double).

    Returns:
        (ndarray, ndarray): tuple contaning the input image and energy image,
            respectively, with the width reduced by one pixel.

    """

    rows, columns, channels = im.shape
    cumulativeEnergyMap = cm.cumulative_minimum_energy_map(energyImage, "VERTICAL")
    verticalSeam = vs.find_optimal_vertical_seam(cumulativeEnergyMap)
    resultimg = np.zeros((rows, columns-1, channels))
    resulteng = np.zeros((rows, columns-1))
    for i in range(rows):
        column = verticalSeam[i]
        resultimg[i, :column, :] = im[i, :column, ]
        resultimg[i, column:] = im[i, column + 1:]
        resulteng[i, :column] = energyImage[i, :column]
        resulteng[i, column:] = energyImage[i, column + 1:]
    return resultimg, resulteng
