# Import libraries
import os
import random
import shutil

# Define the source folders
image_folder = r"C:\Users\josha\Downloads\contamination_data - Copy\images" # Change this to your image folder name
label_folder = r"C:\Users\josha\Downloads\contamination_data - Copy\labels" # Change this to your label folder name

# Define the destination folders
train_image_folder = r"C:\Users\josha\Downloads\zeroWaste_contamination_data\train" # Change this to your train image folder name
test_image_folder = r"C:\Users\josha\Downloads\zeroWaste_contamination_data\test" # Change this to your test image folder name
val_image_folder = r"C:\Users\josha\Downloads\zeroWaste_contamination_data\val" # Change this to your validation image folder name
train_label_folder = r"C:\Users\josha\Downloads\zeroWaste_contamination_data\train_labels" # Change this to your train label folder name
test_label_folder = r"C:\Users\josha\Downloads\zeroWaste_contamination_data\test_labels" # Change this to your test label folder name
val_label_folder = r"C:\Users\josha\Downloads\zeroWaste_contamination_data\val_labels" # Change this to your validation label folder name

# Create the destination folders if they don't exist
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(test_label_folder, exist_ok=True)
os.makedirs(val_label_folder, exist_ok=True)

# Define the split ratios
train_ratio = 0.7 # Change this to your train ratio
test_ratio = 0.2 # Change this to your test ratio
val_ratio = 0.1 # Change this to your validation ratio

# Define a function to split a pair of folders into train/test/val subfolders
def split_pair(image_source_folder, label_source_folder, image_dest_folder, label_dest_folder):
    # Get the list of files in the image source folder
    files = os.listdir(image_source_folder)
    # Shuffle the files randomly
    random.shuffle(files)
    # Calculate the number of files for each split
    train_count = int(len(files) * train_ratio)
    test_count = int(len(files) * test_ratio)
    val_count = len(files) - train_count - test_count
    # Copy the files to the corresponding subfolders
    for i, file in enumerate(files):
        image_src_path = os.path.join(image_source_folder, file)
        label_src_path = os.path.join(label_source_folder, file)
        if i < train_count:
            image_dst_path = os.path.join(image_dest_folder, train_image_folder, file)
            label_dst_path = os.path.join(label_dest_folder, train_label_folder, file)
        elif i < train_count + test_count:
            image_dst_path = os.path.join(image_dest_folder, test_image_folder, file)
            label_dst_path = os.path.join(label_dest_folder, test_label_folder, file)
        else:
            image_dst_path = os.path.join(image_dest_folder, val_image_folder, file)
            label_dst_path = os.path.join(label_dest_folder, val_label_folder, file)
        shutil.copy(image_src_path, image_dst_path)
        shutil.copy(label_src_path, label_dst_path)

# Split the pair of folders individually
split_pair(image_folder, label_folder, image_folder, label_folder)

# Print a message when done
print("Splitting done!")