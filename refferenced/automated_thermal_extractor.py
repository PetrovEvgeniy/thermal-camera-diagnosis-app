import os
import subprocess

# Define the directory containing the images
image_directory = 'C:/Users/PEE1UL/Desktop/thermal_images'

# Define the command template
command_template = 'python flir_image_extractor.py -i {image_path}'

# Loop through all files in the directory
for filename in os.listdir(image_directory):
    # Construct the full file path
    file_path = os.path.join(image_directory, filename)
    
    # Check if the file is an image (you can extend this list with more image extensions if needed)
    if filename.lower().endswith(('.jpg')):
        # Construct the command by replacing the placeholder with the actual file path
        command = command_template.format(image_path=file_path)
        
        # Execute the command
        subprocess.run(command, shell=True)
        
