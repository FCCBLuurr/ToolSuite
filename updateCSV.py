import pandas as pd
import numpy as np
import os

class DataAnalyzer:
    def __init__(self):
        self.df = None
        self.payload_files = None
    
    # Build this function in pandas
    def csv_dataframe(self, csv_url):
        self.df = pd.read_csv(csv_url)

    def create_payload_array(self, payload_directory):
        payload_files = []
        for filename in os.listdir(payload_directory):
            clean_filename = filename.replace('GCE#', '').replace('_1', '').replace('_2', '')
            payload_files.append(clean_filename)

        self.payload_files = np.unique(payload_files)

class DataModifier:
    def __init__(self):
        self.placeholder = None
    
    def compare_dfs(self, csv_data, payload_data):
        pass

# Example usage:
analyzer = DataAnalyzer()

# Create the DataFrame from a CSV accessed via URL
csv_url = "https://example.com/data.csv"
csv_data = analyzer.csv_dataframe(csv_url)


# Create the Payload array
payload_directory = "C:/Payload"
payload_data = analyzer.create_payload_array(payload_directory)
