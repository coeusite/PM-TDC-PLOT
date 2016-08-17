import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


def plot(data, vmin=0, vmax=1.5):
    '''plot function

        This is the plot function of this project.

        Args:
            data: adjusted pandas.DataFrame

        Returns:
            NULL
    '''
    # plot samples
    plt.imshow(np.flipud(data.values.transpose()),
                cmap="jet", interpolation='none',
                vmin=vmin, vmax=vmax,
                extent=[0, 100, -1, 3], aspect="auto")
    plt.xlabel("Time")
    plt.ylabel("log(Diameters)")
    cbar = plt.colorbar(orientation='horizontal')
    cbar.set_label('d N / d log(diameters)')
    plt.show()
    return
