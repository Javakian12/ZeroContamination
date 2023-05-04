# Import os and numpy modules to access files and arrays
import os
import numpy as np
# Import PIL and cv2 modules to handle images and masks
from PIL import Image
import cv2

test = 0

# Define the folder where the green images (masks) are located
mask_folder = R"C:\Users\josha\Downloads\images"

# Define the folder where the other images are located
img_folder = R"C:\Users\josha\Downloads\Output"

# Loop over each file in the mask folder
for file in os.listdir(mask_folder):
  # Get the full path of the file
  file_path = os.path.join(mask_folder, file)
  # Check if the file is an image by its extension
  if file_path.endswith(".jpg") or file_path.endswith(".png"):
    # Get the characters from index 15 to 29 of the file name
    file_prefix = file[:15]
    # Find the matching image in the img folder by using the prefix
    # Try to find the matching image in the img folder by using the prefix
    try:
        img_file = [f for f in os.listdir(img_folder) if f[15:30] == file_prefix][0]
        # Get the full path of the matching image
        img_file_path = os.path.join(img_folder, img_file)
        # Proceed with the rest of the code
    except IndexError:
        # If no match is found, print a message and skip the file
        print(f"No matching image found for {file}")
        continue
    # Get the full path of the matching image
    img_file_path = os.path.join(img_folder, img_file)

    # Read the mask image as a numpy array
    mask_array = np.array(Image.open(file_path))
    # Convert the mask array to grayscale
    mask_gray = cv2.cvtColor(mask_array, cv2.COLOR_BGR2GRAY)
    # Threshold the mask array to get a binary mask of green pixels
    _, mask_binary = cv2.threshold(mask_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Read the other image as a numpy array
    img_array = np.array(Image.open(img_file_path))
    # Convert the other image array to grayscale
    img_gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    # Threshold the other image array to get a binary mask of non-black pixels
    _, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Perform a bitwise AND operation on the two binary masks to get a mask of overlapping pixels
    overlap_mask = cv2.bitwise_and(mask_binary, img_binary)
    # Count the number of non-zero pixels in the overlap mask
    overlap_count = np.count_nonzero(overlap_mask)
    # Check if there are any overlapping pixels
    if overlap_count > 20:
        # Keep the image in the folder
       # print(f"Keeping {img_file} as it has {overlap_count} green pixels that overlap with non-black pixels.")
        # Define a new file name with the prefix and the extension
        new_file = f'{file_prefix}.jpg'
        # Get the full path of the new file for the mask image
        new_mask_file_path = os.path.join(mask_folder, new_file)
        # Get the full path of the new file for the other image
        new_img_file_path = os.path.join(img_folder, new_file)
        # Set a counter to keep track of the number of copies
        counter = 1
        # Loop until the new file name is unique in the img folder
        while os.path.exists(new_img_file_path):
            # Split the file name and extension
            file_name, file_ext = os.path.splitext(new_file)
            # Add an underscore and the counter to the file name
            file_name += f'_{counter}'
            # Increment the counter
            counter += 1
            # Rejoin the file name and extension
            new_file = file_name + file_ext
            # Update the file paths
            new_mask_file_path = os.path.join(mask_folder, new_file)
            new_img_file_path = os.path.join(img_folder, new_file)
        # Rename the mask image file
        os.rename(file_path, new_mask_file_path)
       # print(f"Renamed {file} to {new_file}")
        # Rename the other image file
        os.rename(img_file_path, new_img_file_path)
       # print(f"Renamed {img_file} to {new_file}")
    else:
        # Delete the image from the folder
        os.remove(img_file_path)
        print(f"Deleting {img_file} as it has no green pixels that overlap with non-black pixels.")

