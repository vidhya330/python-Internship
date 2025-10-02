Image Resizer Tool

Description:
A Python script that resizes and optionally converts images in batch. It automates image resizing tasks and saves the processed images in a separate folder.

Tools Used:

Python

Pillow (PIL)

How It Works:

1 Place all images you want to resize in the input folder (input_images).

2 Run the script:

python image_resizer.py

3 The resized images will be saved automatically in the output folder (resized_images).

Features:

1 Resize all images in a folder at once.

2 Optional: Convert images to a different format (JPEG, PNG, etc.).

3 Supports common image formats: JPG, PNG, BMP, GIF, etc.

Folder Structure Example:

project_folder/
│
├── image_resizer.py
├── input_images/      # Place original images here
└── resized_images/    # Resized images will be saved here


How to Customize:

1 Change new_width and new_height in the script to set the resized dimensions.

2 Change convert_format to convert images to another format (or leave None to keep original format).

Outcome:
Automates image resizing and conversion for batch processing, saving time and effort.