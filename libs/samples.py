import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from libs import _outputs

def gaussian(x, mu, sig):
    # calculating probability of Gaussian distribution
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

def generate():
    '''generate function

        This is the sample generator function.

        Args:
            NULL

        Returns:
            data (pd.DataFrame)
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
    # times stamp
    tmp = np.linspace(0, x_length - 1, x_length)
    time_stamp = np.datetime64('2015-01-01T00:00') + [5*i for i in range(201)]
    # transform matrix to pd.DataFrame
    data = pd.DataFrame(data=counts, index=time_stamp,
                        columns=np.array(diameters.round(2), dtype=np.str))
    data.to_csv("sample/data.csv", encoding='utf-8')
    # plot and save
    _outputs.plot(data, png_path="sample/figure.png")
    return data

'''
from importlib import reload;
samples = reload(samples);
data = samples.generate()

from importlib import reload;
data = pd.read_csv("sample/data.csv", encoding='utf-8', index_col=0);
_outputs = reload(_outputs);
_outputs.plot(data, png_path="sample/figure.png");
'''
