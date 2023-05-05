from PIL import Image
import os
import shutil

def get_overlap(image, mask, filename, oldfilename):
    # Get the width and height of the image
    width, height = image.size

    print(filename)

    overlap_pixels = 0
    # Loop over all the pixels in the image
    for x in range(width):
        for y in range(height):
            # Save the modified image
            # Get the RGB values of the pixel at (x, y)
            r1, g1, b1 = image.getpixel((x, y))
            r2, g2, b2 = mask.getpixel((x, y))
            
            # Print the RGB values of the pixel
            if (r1 != 0 or g1 != 0 or b1 != 0) and (r2 == 0 and g2 == 255 and b2 == 0):
                overlap_pixels += 1
    if(overlap_pixels >= 70):
        print("Overlap pixels:", overlap_pixels)
        err = rename_files(image, mask, filename, oldfilename)
        crop_overlap(image, mask, filename)
        move_mask(filename)
        
    return overlap_pixels

def delete_file(filename):
    image_folder_path = R"C:\Users\josha\Downloads\test1" + "\\" + filename
    if os.path.exists(image_folder_path):
        os.remove(image_folder_path)
        print("Deleted File:")
        print(image_folder_path)
        print("-----------------------------")
        
def move_mask(maskFile):
    new_mask_folder_path = R"C:\Users\josha\Downloads\finished_masks"
    mask_folder_path = R"C:\Users\josha\Downloads\test2"
    if os.path.exists(new_mask_folder_path+'\\' + maskFile):
        print("File already exists!")
    else:
        shutil.move(mask_folder_path + "\\" + maskFile, new_mask_folder_path)

def loop_over_folders():
# Iterate over all the files in the folder
    for filename in os.listdir(image_path):
        # Check if the file is an image file
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            delete_file_int = 1
            for maskFile in os.listdir(mask_path):
                if maskFile.endswith('.jpg') or maskFile.endswith('.jpeg') or maskFile.endswith('.png'):
                    if(maskFile[:15] == filename[15:30]):
                        delete_file_int = 0
                        # Load the image file
                        image = Image.open(os.path.join(image_path, filename))
                        mask = Image.open(os.path.join(mask_path, maskFile))

                        # Display the image
                        get_overlap(image, mask, filename, maskFile)
                        print("-----------------------------")
                        
            if(delete_file_int == 1):
                delete_file(filename)


def crop_overlap(image, mask, imageName):
    mask_folder_path = R"C:\Users\josha\Downloads\test2"
    # Get the width and height of the image
    width, height = image.size
    # Loop over all the pixels in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixel at (x, y)
            r1, g1, b1 = image.getpixel((x, y))
            r2, g2, b2 = mask.getpixel((x, y))
            
            # Print the RGB values of the pixel
            if (r1 == 0 and g1 == 0 and b1 == 0) and (r2 == 0 and g2 == 255 and b2 == 0):
                #make mask pixels red
                # Change the pixel at (100, 100) to red
                mask.putpixel((x, y), (165, 42, 42))

    # Save the modified image
    mask.save(mask_folder_path + '\\' + imageName)
    


def rename_files(mask, image, newfilename, oldfilename):
    # Set the path to the folder containing the images
    mask_folder_path = R"C:\Users\josha\Downloads\test2"
    finished_mask_folder_path = r"C:\Users\josha\Downloads\finished_masks"


    # Check if the file is an image file
    if oldfilename.endswith('.jpg') or oldfilename.endswith('.jpeg') or oldfilename.endswith('.png'):
        # Rename the file
        old_file = os.path.join(mask_folder_path, oldfilename)
        new_file = os.path.join(mask_folder_path, newfilename)
        os.rename(old_file, new_file)
        #os.rename(os.path.join(image_folder_path, newfilename), os.path.join(mask_folder_path, filename))


if __name__ == "__main__":
    # Set the path to the folder containing the images
    image_path = R'C:\Users\josha\Downloads\test1'
    mask_path = R'C:\Users\josha\Downloads\test2'
    loop_over_folders()
