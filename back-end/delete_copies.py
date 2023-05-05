'''import os

# define folders
folder1 = r'C:\Users\josha\Downloads\test2'
folder2 = r'C:\Users\josha\Downloads\test1'

# get file names in folder1
file_names = os.listdir(folder1)

# loop through files in folder2
for file in os.listdir(folder2):
    # check if file name is in folder1
    if file not in file_names:
        # delete file from folder2
        os.remove(os.path.join(folder2, file))
        print(f"Deleted file: {file}")'''



import os
import shutil

# define folders
folder1 = r'C:\Users\josha\Downloads\test2'
folder2 = r'C:\Users\josha\Downloads\test1'


# Define the path of the output folder
output_folder = r'C:\Users\josha\Downloads\tester'

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