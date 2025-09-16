import cv2
import os

# Load an image from file
img = cv2.imread('sample_image.jpg')

# Check if image was loaded successfully
if img is None:
    print("Error: Could not load image. Please check the file path.")
else:
    print("Image loaded successfully.")
    
    # Save the image with a new name
    output_filename = 'processed_image.jpg'
    success = cv2.imwrite(output_filename, img)
    
    if success:
        print(f"Image saved as {output_filename}")
        # Verify the file was saved
        if os.path.exists(output_filename):
            print(f"Verified: {output_filename} exists")
        else:
            print(f"Warning: {output_filename} was not found after saving")
    else:
        print("Error: Failed to save the image")
