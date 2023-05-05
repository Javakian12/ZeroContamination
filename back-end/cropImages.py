'''
#crop to box
from pycocotools.coco import COCO
from PIL import Image
import numpy as np

# Load the COCO JSON file
coco = COCO ('_annotations.coco.json')

imge = Image.open ('06_frame_045400_PNG.rf.c8ff168c46bd3f660c55d8ec56b52fd4.jpg')

# Get the image id and file name
img_id = 2411 # change this to your image id
img = coco.imgs [img_id]
img_file = img ['file_name']

# Get the annotation ids and annotations for the image
ann_ids = coco.getAnnIds (imgIds=img_id)
anns = coco.loadAnns (ann_ids)

# Loop over the annotations and edit the image
for ann in anns:
  # Get the category name, confidence score, and coordinates
  cat_id = ann ['category_id']
  cat_name = coco.cats [cat_id] ['name']
  score = ann.get('score', 1.0)
  coords = ann ['bbox']

  # Convert the coordinates to left, top, right, bottom format
  left, top, width, height = coords
  right = left + width
  bottom = top + height

  # Convert the annotation to a binary mask
  mask = coco.annToMask (ann)

  # Read the image
  #img = Image.open (img_file)
  img = Image.open ('06_frame_045400_PNG.rf.c8ff168c46bd3f660c55d8ec56b52fd4.jpg')

  # Crop the image by the mask coordinates
  cropped_img = img.crop ((left, top, right, bottom))

  # Create a new image with the same size as the original image and fill it with black color
  black_bg = Image.new ('RGB', img.size, (0, 0, 0))

  # Paste the cropped image onto the black background using the same coordinates
  #black_bg.paste (cropped_img, (left, top, right, bottom))
  black_bg.paste (cropped_img, (round (left), round (top), round (right), round (bottom)))

  # Save the edited image with a new file name
  new_file = f'{cat_name}_{score:.2f}_{img_file}'
  black_bg.save (new_file)

#crop single image to mask
from pycocotools.coco import COCO
import numpy as np
from PIL import Image

# Load the COCO JSON file
coco = COCO ('_annotations.coco.json')

# Get the image id and file name
img_id = 3379 # change this to your image id
img = coco.imgs [img_id]
img_file = img ['file_name']

# Get the annotation ids and annotations for the image
ann_ids = coco.getAnnIds (imgIds=img_id)
anns = coco.loadAnns (ann_ids)

# Loop over the annotations and edit the image
for ann in anns:
  # Get the category name, confidence score, and segmentation mask
  #cat_id = ann ['category_id'] #if you want to run on all attributes
  #cat_name = coco.cats [cat_id] ['name'] #if you want to run on all attributes
  cat_id = 1 #if you want to run on just cardboard
  cat_name = 'cardboard' #if you want to run on just cardboard
  score = ann.get ('score', 1.0) # use 1.0 as the default score if not found
  segm = ann ['segmentation']

  # Convert the segmentation mask to a binary mask
  mask = coco.annToMask (ann)

  # Read the image as a numpy array
  img_array = np.array (Image.open (img_file))

  # Apply the mask to the image and make the rest of the image black
  masked_img_array = np.where (mask[:, :, np.newaxis] == 1, img_array, 0)

  # Convert the masked image array back to an image
  masked_img = Image.fromarray (masked_img_array)

  # Save the masked image with a new file name
  new_file = f'{cat_name}_{score:.2f}_{img_file}'
  masked_img.save (new_file) '''

#crop folder to mask
from pycocotools.coco import COCO
import numpy as np
from PIL import Image
import os # import os module to access files and directories

os.chdir(r'C:\Users\josha\Downloads')
# Load the COCO JSON file
coco = COCO (r'C:\Users\josha\Downloads\test1\_annotations.coco.json')

# Create a dictionary to store the file names and image ids
file_to_id = {}
# Loop over the images in the COCO JSON filen 
for img in coco.imgs.values():
  # Get the file name and image id
  file_name = img['file_name']
  img_id = img['id']
  # Add them to the dictionary
  file_to_id[file_name] = img_id

# Define the folder where the images are located
img_folder = r'C:\Users\josha\Downloads\test1'

# Loop over each file in the folder
for file in os.listdir(img_folder):
  # Get the full path of the file
  file_path = os.path.join(img_folder, file)
  # Check if the file is an image by its extension
  if file_path.endswith(".jpg") or file_path.endswith(".png"):
    # Get the image id and file name from the dictionary
    img_id = file_to_id[file]
    img_file = file

    # Get the annotation ids and annotations for the image
    ann_ids = coco.getAnnIds (imgIds=img_id)
    anns = coco.loadAnns (ann_ids)

    # Loop over the annotations and edit the image
    for ann in anns:
      # Get the category name, confidence score, and segmentation mask
      #cat_id = ann ['category_id'] #if you want to run on all attributes
      #cat_name = coco.cats [cat_id] ['name'] #if you want to run on all attributes
      cat_id = 1 #if you want to run on just cardboard
      cat_name = 'cardboard' #if you want to run on just cardboard
      score = ann.get ('score', 1.0) # use 1.0 as the default score if not found
      segm = ann ['segmentation']

      # Convert the segmentation mask to a binary mask
      mask = coco.annToMask (ann)

      # Read the image as a numpy array
      print(img_file)
      img_array = np.array (Image.open (img_folder+'\\'+img_file))

      # Apply the mask to the image and make the rest of the image black
      masked_img_array = np.where (mask[:, :, np.newaxis] == 1, img_array, 0)

      # Convert the masked image array back to an image
      masked_img = Image.fromarray (masked_img_array)

      # Save the masked image with a new file name
      new_file = f'{cat_name}_{score:.2f}_{img_file}'
      #check if file exists with same name
      #if yes, change name + 1,
      #else make image
      # Define the output folder where the masked images will be saved
      output_folder = r'C:\Users\josha\downloads\Output'
      # Get the full path of the new file
      new_file_path = os.path.join(output_folder, new_file)
      # Set a counter to keep track of the number of copies
      counter = 1
      # Loop until the file name is unique
      while os.path.exists(new_file_path):
        # Split the file name and extension
        file_name, file_ext = os.path.splitext(new_file)
        # Add an underscore and the counter to the file name
        file_name += f'_{counter}'
        # Increment the counter
        counter += 1
        # Rejoin the file name and extension
        new_file = file_name + file_ext
        # Update the file path
        new_file_path = os.path.join(output_folder, new_file)
      # Save the masked image to the output folder
      masked_img.save (new_file_path)