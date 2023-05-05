import os
from PIL import Image
from PIL import ImageChops

def get_green_box(image):
    # Convert image to RGBA format
    rgba_image = image.convert('RGBA')

    # Get the dimensions of the image
    width, height = rgba_image.size

    # Define the coordinates of the green area
    # Replace these values with the coordinates of the green area in your images
    left = 0
    top = 0
    right = width // 2
    bottom = height // 2

    return (left, top, right, bottom)

def images_match(img_x, img_y, threshold):
    diff = ImageChops.difference(img_x, img_y)
    non_black_pixels = 0
    for pixel in diff.getdata():
        if pixel != (0, 0, 0):
            non_black_pixels += 1
    
    return non_black_pixels <= threshold


green_threshold = 10 # adjust this threshold to control how much green is required for a match

for image_x in os.listdir(R"C:\Users\josha\Downloads\test2"):
    if image_x.endswith(".png") or image_x.endswith(".jpg"):
        x_path = os.path.join(R"C:\Users\josha\Downloads\test2", image_x)
        x_image = Image.open(x_path)

        green_pixels = 0
        for pixel in x_image.getdata():
            if pixel == (0, 255, 0):
                green_pixels += 1
        for image_y in os.listdir(R"C:\Users\josha\Downloads\test1"):
            if image_y.endswith(".png") or image_y.endswith(".jpg"):
                y_path = os.path.join(R"C:\Users\josha\Downloads\test1", image_y)
                y_image = Image.open(y_path)

                # crop the green area from both images
                x_crop = x_image.crop(get_green_box(x_image))
                y_crop = y_image.crop(get_green_box(y_image))

                # compare the two cropped regions
                if images_match(x_crop, y_crop, green_threshold):
                    # rename the files if they match
                    os.rename(x_path, os.path.join(R"C:\Users\josha\Downloads\test2", "match_" + image_x))
                    os.rename(y_path, os.path.join(R"C:\Users\josha\Downloads\test1", "match_" + image_y))
                    break
                else:
                    # delete the image_y file if no match was found
                    y_crop_diff = ImageChops.difference(y_crop, Image.new('RGB', y_crop.size, (0, 0, 0)))
                    if sum(y_crop_diff.getdata()) > 0:
                        # check if there are at least 10 non-black pixels in the cropped region of image_y
                        non_black_pixels = 0
                        for pixel in y_crop_diff.getdata():
                            if pixel != (0, 0, 0):
                                non_black_pixels += 1
                        if non_black_pixels <= green_threshold:
                            os.remove(y_path)
                            break
