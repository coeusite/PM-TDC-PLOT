import pandas as pd

def csv_to_dataframe(file_name, encoding=None):
    '''load function

        This function load csv data to numpy matrix

        Args:
            file_name: the path of csv file
            encoding: encoding of the csv file, default is None

        Returns:
            data: numpy matrix
    '''
    data = pd.read_csv(file_name, encoding=encoding)
    return data
