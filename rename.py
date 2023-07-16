import os
import re
import sys
from tqdm import tqdm

def get_file_list(folder_path):
    files = os.listdir(folder_path)
    return files

def rename_files(folder_path, start_number, files):        
    files.sort(key=lambda x: int(re.findall(r'\d+', x)[0]))
    
    # Initialize the counter
    count = start_number
    i = 1

    total_files = len(files)
    
    for file_name in files:
        # Generate the new file names with i iterating and resetting
        if i == 1:
            new_name_1 = f"GCE#{count}_{i}.CR2"
            current_path = os.path.join(folder_path, file_name)
            new_path_1 = os.path.join(folder_path, new_name_1)
            os.rename(current_path, new_path_1)
            i += 1
        elif i == 2:
            new_name_2 = f"GCE#{count}_{i}.CR2"
            current_path = os.path.join(folder_path, file_name)
            new_path_2 = os.path.join(folder_path, new_name_2)
            os.rename(current_path, new_path_2)
            count += 1
            i = 1
        
    return total_files

if __name__ == "__main__":
    folder_path = "C:/payload"  # Specify the path to your folder
    start_number = int(sys.argv[1])
    files = get_file_list(folder_path)
    rename_files(folder_path, start_number, files)
