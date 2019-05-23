import numpy as np
import cumulative_minimum_energy_map as cm
import find_optimal_horizontal_seam as hs

def reduceHeight(im, energyImage):

    """ Reduces the height of the input image and the energy image by one pixel.

    Args:
        im (ndarray): Image too be reduced (size: MxNx3, type:uint8).
        energyImage (ndarray): 2D matrix containing energies of each pixel
            (size: MxN, type:double).

    Returns:
        (ndarray, ndarray): tuple contaning the input image and energy image,
            respectively, with the height reduced by one pixel.

    """

    rows, columns, channels = im.shape
    cumulativeEnergyMap = cm.cumulative_minimum_energy_map(energyImage, "HORIZONTAL")
    horizontalSeam = hs.find_optimal_horizontal_seam(cumulativeEnergyMap)
    resultimg = np.zeros((rows-1, columns, channels))
    resulteng = np.zeros((rows-1, columns))
    for i in range(columns):
        row = horizontalSeam[i]
        resultimg[:row, i, :] = im[:row, i, ]
        resultimg[row:, i] = im[row+1:, i]
        resulteng[:row, i] = energyImage[:row, i]
        resulteng[row:, i] = energyImage[row+1:, i]
    return resultimg, resulteng
