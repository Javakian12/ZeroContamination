

import os
import shutil

# define folders
folder1 = r'C:\Users\josha\Downloads\tester'
folder2 = r'C:\Users\josha\Downloads\test1'


# Define the path of the output folder
output_folder = r'C:\Users\josha\Downloads\tester_labels'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Loop through the files in the first folder
for filename in os.listdir(folder1):
    # Get the full path of the file in the first folder
    file1 = os.path.join(folder1, filename)
    
    # Get the full path of the file in the second folder
    file2 = os.path.join(folder2, filename)

    # Check if the file exists in both folders
    if os.path.isfile(file1) and os.path.isfile(file2):
        # Move the file to the output folder
        shutil.move(file1, output_folder)
        print(f"Moved {filename} to {output_folder}")