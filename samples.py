import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def generate():
    # log(diameters): (-1, 3)
    # counts = d N/d log(diameters): gaussian(mu|t, 0.1)
    # (x, y, color) = (time, diameters, counts)
    x_length = 200
    y_length = 100
    # vector
    times = np.linspace(0, 100, x_length)
    diameters = np.linspace(-1, 3, y_length)
    # matrix
    times_matrix = np.tile(times, (y_length ,1)).transpose()
    diameters_matrix = np.tile(diameters, (x_length, 1))
    # generate random sample
    sig = 0.2
    mu_matrix = np.log(times_matrix + 1) / 5 * 4 - 1
    counts = gaussian(diameters_matrix, mu_matrix, sig)
    counts += np.random.normal(np.ones((x_length, y_length)), sig) / 5
    # plot samples
    plt.imshow(np.flipud(counts.transpose()),
                    cmap="jet", interpolation='none',
                    extent=[0, 100, -1, 3], aspect="auto")
    plt.xlabel("Time")
    plt.ylabel("log(Diameters)")
    plt.show()
    # transform matrix to pd.DataFrame
    df = pd.DataFrame(data=counts, index=times, columns=diameters)
    return
    
