import pandas as pd
import numpy as np
import os
import sys
from collections import OrderedDict

class DataAnalyzer:

    def file_array(self, folder_path):
        folder_list = []
        for filename in os.listdir(folder_path):
            clean_filename = filename.replace('GCE#', '').replace('_1', '').replace('_2', '').replace('.jpg','').replace('cr2','')
            folder_list.append(clean_filename)

        clean_list = list(OrderedDict.fromkeys(folder_list))
        folder_array = list(map(int, clean_list))
        folder_numpy = np.array(folder_array)

        print("Folder List:")
        print(folder_numpy)
        return folder_numpy

    def test_df(self, csv_url, start_row=(), num_rows=()):
        test_df = pd.read_csv(csv_url, usecols=['ITEM ID', 'Photo Shoot? Y/N'])
        test_array = test_df['ITEM ID'].to_numpy()

        print("List of ITEM IDs:")
        print(test_array)
        return test_array, test_df

class DataModifier:

    def compare_arrays(self, arr1, arr2):

        print("CSV Array:", arr1)
        print("File list:", arr2)
        boolean_array = np.equal(arr1, arr2)
        
        print("Boolean array test:", boolean_array)
        print(len(data_analyzer.file_array(folder_path)))
        return boolean_array

    def modify_photo_yes(self, start_number, csv_array, file_array, test_df ):
        
        i = start_number
        if len(csv_array) == len(file_array):
            while csv_array[i] == file_array[i]:
                
        
        else:
            print("Array values are invalid")
        
        
        return



if __name__ == "__main__":
    data_analyzer = DataAnalyzer()
    data_modifier = DataModifier()

    folder_path = 'C:/payload'
    csv_url = 'C:/test.csv'

    test_array = data_analyzer.test_df(csv_url)
    folder_numpy = data_analyzer.file_array(folder_path)
    test_df = data_analyzer.test_df

    ## Add ` int(sys.argv[1]) if len(sys.argv) > 1 else 0 ` when implementing, without backticks
    start_number = sys.argv[1]
    start_row = 2
    num_rows = folder_numpy if start_row > 1 else None
    data_modifier.compare_arrays(test_array, folder_numpy)