import os
from PIL import Image

input_folder = "input_images"    # Folder containing original images
output_folder = "resized_images" # Folder to save resized images
new_width = 800                  # New width for the images
new_height = 600                 # New height for the images
convert_format = None            # e.g., 'JPEG', 'PNG', or None to keep original


if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        with Image.open(file_path) as img:
            # Resize the image
            img_resized = img.resize((new_width, new_height))
        
            if convert_format:
                save_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.' + convert_format.lower())
                img_resized.save(save_path, convert_format)
            else:
                save_path = os.path.join(output_folder, filename)
                img_resized.save(save_path)
        
        print(f"Resized and saved: {save_path}")

print("All images have been resized successfully!")
