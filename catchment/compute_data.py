"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
    data = data_dir.load_catchment_data()

    daily_standard_deviation = compute_standard_deviation_by_day(data)

    return daily_standard_deviation


def daily_std(dataset):
    daily_std = dataset.groupby(dataset.index.date).std()
    return daily_std


def compute_standard_deviation_by_day(data):
    daily_std_list = map(daily_std, data)
    daily_standard_deviation = pd.concat(daily_std_list)
    return daily_standard_deviation


def load_catchment_data(data_dir):
    data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    if len(data_file_paths) == 0:
        raise ValueError('No CSV files found in the data directory')
    data = map(models.read_variable_from_csv, data_file_paths)
    return data


class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No CSV files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return data


class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return data
