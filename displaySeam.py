import numpy as np
import matplotlib.pyplot as plt
import cumulative_minimum_energy_map as cm
import energy_image as ei


def displaySeam(im, seam, type):

    """ Displays the seam on top of an image.

    Args:
        im (ndarray): Input image (size: MxNx3, type:uint8).
        seam (list): Vector containing the row/column indices for the seam.
        type (string): Direction of the seam: ‘HORIZONTAL’ or ‘VERTICAL.

    """

    rows, columns, channels = im.shape
    fig, ax = plt.subplots()
    imgplot = ax.imshow(im)
    if type is "VERTICAL":
        ax.plot(seam, range(rows))
    if type is "HORIZONTAL":
        ax.plot(range(columns), seam)
    plt.show()
