"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import pandas as pd

from catchment import models, views

class CSVDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path 
    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_csv, data_file_paths)
        return list(data)
    
class JSONDataSource:
    """
    Loads patient data with catchment values from JSON files within a specified folder.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_catchment_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'rain_data_2015*.json'))
        if len(data_file_paths) == 0:
            raise ValueError('No JSON files found in the data directory')
        data = map(models.read_variable_from_json, data_file_paths)
        return list(data)
    
    # def load_catchment_data(self):
    #     data_file_paths = glob.glob(os.path.join(self.data_dir, 'rain_data_2015*.csv'))
    #     if len(data_file_paths) == 0:
    #         raise ValueError('No CSV files found in the data directory')
    #     return data_file_paths

    # def load_catchment_data(data_dir):
    # data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    # if len(data_file_paths) == 0:
    #     raise ValueError('No CSV files found in the data directory')
    # return data_file_paths

def analyse_data(dir_path):
    """Calculate the standard deviation by day between datasets.

    Gets all the measurement data from the CSV files in the data directory,
    works out the mean for each day, and then graphs the standard deviation
    of these means.
    """
   # data_file_paths = glob.glob(os.path.join(data_dir, 'rain_data_2015*.csv'))
    #if len(data_file_paths) == 0:
     #   raise ValueError('No CSV files found in the data directory')
   # load_catchment_data(data_dir)
   # data = map(models.read_variable_from_csv, load_catchment_data(data_dir))
    data = dir_path.load_catchment_data()
    #data = map(models.read_variable_from_csv, data_dir.load_catchment_data())
    daily_standard_deviation = compute_standard_deviation_by_day(data)
    return daily_standard_deviation

def compute_standard_deviation_by_day(data):
    
   # daily_std_list = []
    #for dataset in data:
     #   daily_std = dataset.groupby(dataset.index.date).std()
      #  daily_std_list.append(daily_std)
    
    daily_std_list = map(models.daily_std, data)
    daily_standard_deviation = pd.concat(daily_std_list)

    return daily_standard_deviation

    #graph_data = {
     #   'daily standard deviation': daily_standard_deviation
    #}

    #views.visualize(graph_data)
