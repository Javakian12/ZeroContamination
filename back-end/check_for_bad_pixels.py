from PIL import Image

# Open the image file
image = Image.open(r"C:\Users\josha\Downloads\zeroWaste_contamination_data\train_labels\cardboard_1.00_04_frame_003010_PNG.rf.fedfdbd26d6723c3af601752e9aa8c34_1_2.jpg")

# Get the RGB data of the image
rgb_data = image.convert('RGB').getdata()

# Count the number of pixels with each color
color_count = {}
for r, g, b in rgb_data:
    color = (r, g, b)
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1

# Sort the colors by count in descending order
sorted_colors = sorted(color_count.items(), key=lambda x: x[1], reverse=True)

# Print the colors and their counts
for color, count in sorted_colors:
    print(f"Color: {color} - Count: {count}")