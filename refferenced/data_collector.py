import requests
import time
import os
from datetime import datetime

# Configuration
CAMERA_IP = '192.168.1.50'  # Replace with your camera's IP address
IMAGE_FORMAT = 'JPEG'       # Use 'FFF' for radiometric data only
IMAGE_INTERVAL = 5        # Time interval between requests in seconds
IMAGE_STORAGE_PATH = 'C:/Users/PEE1UL/Desktop/RawThermalStreamViewer/electric_kettle/'  # Path to output directory  

# Ensure the output directory exists
os.makedirs(IMAGE_STORAGE_PATH, exist_ok=True)

# Function to fetch an image from the camera
def fetch_image():
    url = f'http://{CAMERA_IP}/api/image/current?imgformat={IMAGE_FORMAT}'
    start_time = time.time()
    response = requests.get(url, stream=True)
    fetch_time = time.time() - start_time

    if response.status_code == 200:
        print(f"Image fetched in {fetch_time:.2f} seconds.")
        return response.content
    else:
        print(f'Failed to retrieve image. Status code: {response.status_code}')
        return None

# Function to save an image to disk
def save_image(image_data):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]  # Format: 20240807_130153_605
    filename = f'img_{timestamp}.jpg'
    file_path = os.path.join(IMAGE_STORAGE_PATH, filename)
    
    with open(file_path, 'wb') as file:
        file.write(image_data)
    print(f"Image saved as {filename}")

# Function to continuously fetch and save images
def image_saver():
    while True:
        raw_data = fetch_image()
        #if raw_data is not None:
            #save_image(raw_data)
        time.sleep(IMAGE_INTERVAL)

def main():
    image_saver()

if __name__ == '__main__':
    main()
