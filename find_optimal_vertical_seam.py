import numpy as np

def find_optimal_vertical_seam(cumulativeEnergyMap):

    """ Computes the optimal vertical seam with the least energy.

    Args:
        cumulativeEnergyMap (ndarray): cumulative energy map with the sums
            present in the last row (size: MxN, type:double)

    Returns:
        list: vector containing the column indices of the pixels in each row that
            are a part of the vertical seam starting from the first row

    """

    rows, columns = cumulativeEnergyMap.shape
    result = []
    minColumn = 0
    min = cumulativeEnergyMap[rows-1][minColumn]
    for j in range(1, columns):
        if cumulativeEnergyMap[rows-1][j] < min:
            minColumn = j
            min = cumulativeEnergyMap[rows-1][minColumn]
    result.append(minColumn)
    for i in range(rows - 2, -1, -1):
        min = cumulativeEnergyMap[i][minColumn]
        for j in range(minColumn - 1, minColumn + 2):
            if j >= 0 and j < columns:
                if cumulativeEnergyMap[i][j] < min:
                    minColumn = j
                    min = cumulativeEnergyMap[i][minColumn]
        result.append(minColumn)
    return result[::-1]
