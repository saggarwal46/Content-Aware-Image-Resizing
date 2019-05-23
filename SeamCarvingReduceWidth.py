import numpy as np
import energy_image as ei
import reduceWidth as rw
import matplotlib.pyplot as plt
import sys

def argCheck():
    if len(sys.argv) == 3:
        return ((sys.argv[1][-3:] == "jpg" or sys.argv[1][-4:] == "jpeg")
            and sys.argv[2].isdigit())
    else:
        print("Incorrect number of arguments.")

if __name__ == "__main__":
    if (not argCheck()):
        print("Incorrect arguments passed. Please refer to the README.")
        exit()

    im = plt.imread(sys.argv[1], format='jpeg')
    for i in range(int(sys.argv[2])):
        im, energy_im = rw.reduceWidth(im, ei.energy_image(im.astype(np.uint8)))
    plt.imsave('outputReducedWidth.png', im.astype(np.uint8))
