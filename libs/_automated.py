import pandas as pd
import numpy as np

import fnmatch, os

from libs import _inputs, _outputs

# Constant
DATA_COL_RANGE = [6, 56]


def run():
    '''run function

        This function automatically parse txt files in data/raw/ folder
        and store csv files to data/parsed/ folder. At the same time,
        a corresponding figure would be create in figures/ folder.

    '''
    # TODO(CoeusITE) import txt data to a sqlite database
    auto_parse()
    auto_plot()
    return

def auto_parse():
    '''auto_parse function

    '''
    # parsing
    for file_name in os.listdir('data/raw/'):
        if fnmatch.fnmatch(file_name, '*.txt'):
            # parse data
            data = parse_file('data/raw/{}'.format(file_name))
            # save to csv
            data.to_csv('data/parsed/{}'.format(file_name.replace('.txt', '.csv')), encoding='utf-8')
    return

def auto_plot(show_plot=False):
    '''auto_plot function

    '''
    # plotting
    for file_name in os.listdir('data/parsed/'):
        if fnmatch.fnmatch(file_name, '*.csv'):
            # read data
            data = _inputs.csv_to_dataframe('data/parsed/' + file_name, encoding='utf-8')
            # plot to png
            _outputs.plot(data, png_path='figures/{}'.format(file_name.replace('.csv', '.png')), vmax=1000, show_flag=show_plot)
    return


def parse_file(file_name):
    '''parse_file function

        This function will parse selected data file.

    '''
    encodings = ['utf-8', 'windows-1250', 'windows-1252']
    for e in encodings:
        try:
            fh = codecs.open(file_name, 'r', encoding=e)
            lines = fh.read().split('\r\n')
            fh.close()
        except UnicodeDecodeError:
            print('got unicode error with %s , trying different encoding' % e)
        else:
            print('opening the file with encoding:  %s ' % e)
            break
    data_matrix, header = read_data(lines)
    data = parse_data(data_matrix, header)
    return data


def read_data(lines):
    '''read_data function

        This function will transform text lines to numpy matrix.

        Args:
            lines: a string list of the entire data file

        Returns:
            data_matrix: a matrix of all valid data strings
            header: a list of header strings
    '''
    #
    data_lines = []
    for i in range(len(lines)):
        vector = lines[i].split('\t')
        if vector[0].isdigit():
            if not(i % 1000): print('reading the {}-th data line...'.format(vector[0]))
            data_lines.append(vector)
        elif vector[0] == 'Sample #':
            header = vector
    data_matrix = np.array(data_lines)
    return data_matrix, header


def parse_data(data_matrix, header):
    '''parse_data function

        This function will transform numpy matrix to pandas DataFrame.

        Args:
            data_matrix: a matrix of all valid data strings
            header: a list of header strings

        Returns:
            data: a pandas DataFrame of all valid data
    '''
    print('creating time stamps...')
    time_stamps = pd.to_datetime([' '.join(x) for x in data_matrix[:, 1:3]])
    print('creating numeric data matrix...')
    data = pd.DataFrame(data=np.array(data_matrix[:, DATA_COL_RANGE[0]-1:DATA_COL_RANGE[1]], dtype=np.float),
                        columns=header[DATA_COL_RANGE[0]-1:DATA_COL_RANGE[1]], index=time_stamps)
    return data


'''
for j in [76, 77, 78, 79, 80, 81]:
    col = data_matrix[3280:7300, j] #3280:4426 # 03-22 凌晨 低 mean
    col[col == '-1.#IND'] = '-1'
    col = np.array(col, dtype=np.float)
    col[col==-1] = np.nan
    plt.plot(col)
    plt.title(header[j])
    plt.show()
'''
