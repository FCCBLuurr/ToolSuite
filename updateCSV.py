import csv
import os
import re

class CSVProcessor:
    def __init__(self, csv_file_path, directory_path, column_item_id):
        self.csv_file_path = csv_file_path
        self.directory_path = directory_path
        self.column_item_id = column_item_id

    def get_csv_item_ids(self):
        csv_item_ids = []
        with open(self.csv_file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                item_id = row[self.column_item_id - 1]  # Adjust for 0-based indexing
                csv_item_ids.append(item_id)
        return csv_item_ids

    def get_file_item_ids(self):
        file_item_ids = []
        for filename in os.listdir(self.directory_path):
            file_item = re.findall(r"GCE#(\d+)_\d+", filename)
            if file_item:
                file_item_ids.append(file_item[0])
        file_item_ids = list(set(file_item_ids))  # Remove duplicates
        return file_item_ids

# Usage example
csv_file_path = "C:/launchPad"  # Replace with the actual path to your CSV file
directory_path = "C:/payload"  # Replace with the actual directory path
column_item_id = 4

processor = CSVProcessor(csv_file_path, directory_path, column_item_id)
csv_item_ids = processor.get_csv_item_ids()
file_item_ids = processor.get_file_item_ids()

print("CSV Item IDs:", csv_item_ids)
print("File Item IDs:", file_item_ids)
