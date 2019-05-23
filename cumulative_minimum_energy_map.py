import numpy as np
import matplotlib.pyplot as plt

def cumulative_minimum_energy_map(energyImage, seamDirection):

    """ Computes the cumulative energy map to find vertical/horizontal seams
        with the lowest energies.

    Args:
        energyImage (ndarray): 2D matrix containing energies of each pixel
                               (size: MxN, type:double).
        seamDirection (string): Direction of the seam: ‘HORIZONTAL’ or ‘VERTICAL’.

    Returns:
        ndarray: cumulative energy map with the sums present in the
                 last row/column (size: MxN, type:double).

    """

    if seamDirection == "HORIZONTAL":
        energyImage = energyImage.T
    rows, columns = energyImage.shape
    cumulative_minimum_energy = np.zeros((rows, columns), dtype='float64')
    cumulative_minimum_energy[0] = energyImage[0]
    for i in range(1, rows):
        for j in range(columns):
            val1 = cumulative_minimum_energy[i-1][j - 1] if j > 0 else cumulative_minimum_energy[i-1][j]
            val2 = cumulative_minimum_energy[i-1][j]
            val3 = cumulative_minimum_energy[i-1][j + 1] if j < columns - 1 else cumulative_minimum_energy[i-1][j]
            cumulative_minimum_energy[i][j] = energyImage[i][j] + min(val1, val2, val3)
    if seamDirection == "HORIZONTAL":
        cumulative_minimum_energy = cumulative_minimum_energy.T
    return cumulative_minimum_energy
