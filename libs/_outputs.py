import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



def plot(data, vmin=0, vmax=500, png_path=None, show_flag=True):
    '''plot function

        This is the plot function of this project.

        Args:
            data: adjusted pandas.DataFrame
            vin, vmax: range of the color values

        Returns:
            NULL

        Notes:
            x-axis range = the length of time-series
            y-axis range = (log 0.5, log 20)
    '''
    # plot samples
    fig = plt.figure();
    plt.imshow(data.values.transpose(),
                cmap="jet", interpolation='none', origin='lower',
                vmin=vmin, vmax=vmax, aspect="auto");
    ax = plt.gca();
    # xticks
    xticks = np.array(ax.get_xticks(), dtype=np.int);
    xticks = xticks[xticks >=0]
    xticks = xticks[xticks <= len(data.index)]
    xticks_labels = data.index[xticks];
    plt.xticks(rotation=7.5)
    ax.set_xticks(xticks);
    ax.set_xticklabels(xticks_labels);
    # yticks
    yticks = np.array(ax.get_yticks(), dtype=np.int);
    yticks = yticks[yticks >=0]
    yticks = yticks[yticks <= len(data.columns)]
    yticks_labels = data.columns[yticks];
    ax.set_yticks(yticks);
    ax.set_yticklabels(yticks_labels);
    # labels
    plt.xlabel("Time");
    plt.ylabel("Diameters (micrometer)");
    cbar = plt.colorbar(orientation='horizontal'); #
    cbar.set_label('d N / d log(diameters)');
    # plot
    if png_path: plt.savefig(png_path);
    if show_flag: plt.show();
    plt.close(fig)
    return

def plot_sample(data, vmin=0, vmax=1.5, png_path=None, show_flag=True):
    '''plot function

        This is the plot function of this project.

        Args:
            data: adjusted pandas.DataFrame
            vin, vmax: range of the color values

        Returns:
            NULL

        Notes:
            x-axis range = the length of time-series
            y-axis range = (log 0.5, log 20)
    '''
    # plot samples
    fig = plt.figure();
    plt.imshow(data.values.transpose(),
                cmap="jet", interpolation='none', origin='lower',
                vmin=vmin, vmax=vmax, aspect="auto",
                extent=[0, data.values.shape[0]-1, np.log(0.5), np.log(20)]);
    ax = plt.gca();
    # xticks
    xticks = np.array(ax.get_xticks(), dtype=np.int);
    xticks[-1] = len(data.index) - 1;
    xticks_labels = data.index[xticks];
    plt.xticks(rotation=5)
    ax.set_xticks(xticks);
    ax.set_xticklabels(xticks_labels);
    # yticks
    yticks = np.log([0.5, 1, 2.5, 5, 10, 15, 20]);
    yticks_labels = np.array(np.exp(yticks).round(1), dtype=np.str);
    ax.set_yticks(yticks);
    ax.set_yticklabels(yticks_labels);
    # labels
    plt.xlabel("Time");
    plt.ylabel("Diameters (micrometer)");
    cbar = plt.colorbar(orientation='horizontal'); #
    cbar.set_label('d N / d log(Dp)');
    # plot
    if png_path: plt.savefig(png_path);
    if show_flag: plt.show();
    plt.close(fig)
    return
