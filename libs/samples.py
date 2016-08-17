import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def gaussian(x, mu, sig):
    # calculating probability of Gaussian distribution
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def generate():
    '''generate function

        This is the sample generator function.

        Args:
            NULL

        Returns:
            sample (pd.DataFrame)
                log(diameters): (-1, 3)
                counts = d N/d log(diameters): gaussian(mu|t, 0.1)
                (x, y, z|color) = (time, diameters, counts)
    '''
    x_length = 201
    y_length = 101
    # vector
    times = np.linspace(0, 100, x_length)
    diameters = np.linspace(np.log(0.5), np.log(20), y_length)
    # matrix
    times_matrix = np.tile(times, (y_length ,1)).transpose()
    diameters_matrix = np.tile(diameters, (x_length, 1))
    # generate random sample
    sig = 0.2
    mu_matrix = np.log(times_matrix + 1) / 5 * 4 - 1
    counts = gaussian(diameters_matrix, mu_matrix, sig)
    counts += np.random.normal(np.ones((x_length, y_length)), sig) / 5
    # plot samples
    fig = plt.figure();
    plt.imshow(np.flipud(counts.transpose()),
                cmap="jet", interpolation='none',
                vmin=0, vmax=1.35,
                extent=[0, 100, np.log(0.5), np.log(20)], aspect="auto");
    ax = plt.gca();
    yticks = np.log([0.5, 1, 2, 5, 10, 15, 20]);
    yticks_labels = np.array(np.exp(yticks).round(1), dtype=np.str);
    ax.set_yticks(yticks);
    ax.set_yticklabels(yticks_labels);
    plt.xlabel("Time");
    plt.ylabel("Diameters (micrometer)");
    cbar = plt.colorbar(orientation='horizontal');
    cbar.set_label('d N / d log(diameters)');
    plt.savefig("sample/figure.png")
    plt.show();
    plt.close(fig)
    # transform matrix to pd.DataFrame
    sample = pd.DataFrame(data=counts, index=np.array(times.round(2), dtype=np.str),
                        columns=np.array(diameters.round(2), dtype=np.str))
    sample.to_csv("sample/data.csv", encoding='utf-8')
    return sample

'''
data = pd.read_csv("sample/data.csv", encoding='utf-8', index_col=1);
fig = plt.figure();
plt.imshow(np.flipud(data.values.transpose()),
            cmap="jet", interpolation='none',
            vmin=0, vmax=1.5,
            extent=[0, 100, -1, 3], aspect="auto");
ax = plt.gca();
yticks = np.linspace(np.log(0.5), np.log(20), 6);
yticks_labels = np.array(np.exp(yticks).round(1), dtype=np.str);
ax.set_yticks(yticks);
ax.set_yticklabels(yticks_labels);
plt.xlabel("Time");
plt.ylabel("Diameters (micrometer)");
cbar = plt.colorbar(orientation='horizontal');
cbar.set_label('d N / d log(diameters)');
plt.show();
'''
