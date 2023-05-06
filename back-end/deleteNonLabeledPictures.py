#The purpose of this file is to match the first 15 characters of the filenames so all that is left is
#The mask and its respective image

# Import os module to access files and directories
import os

# Define the source folder where the images to be deleted are located
source_folder = R"C:\Users\josha\Downloads\test1"

# Define the target folder where the images to be matched are located
target_folder = R"C:\Users\josha\Downloads\finished_masks"

# Loop through each file in the source folder
for file in os.listdir(source_folder):
    # Get the full path of the file
    file_path = os.path.join(source_folder, file)
    # Check if the file is an image by its extension
    if file_path.endswith(".jpg") or file_path.endswith(".png"):
        # Get 15-30 characters of the file name
        file_prefix = file
        # Set a flag to indicate if the file has a match in the target folder
        match_found = False
        # Loop through each file in the target folder
        for target_file in os.listdir(target_folder):
            # Get the full path of the target file
            target_file_path = os.path.join(target_folder, target_file)
            # Check if the target file is an image by its extension
            if target_file_path.endswith(".jpg") or target_file_path.endswith(".png"):
                # Get the first 15 characters of the target file name
                target_file_prefix = target_file[15:30]
                # Compare the prefixes of the source and target files
                if file_prefix == target_file_prefix:
                    # If they match, set the flag to True and break the loop
                    match_found = True
                    break
        # If no match is found, delete the source file
        if not match_found:
            os.remove(file_path)
            print(f"Deleted {file_path}")