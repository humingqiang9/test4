import cv2
import numpy as np
import os

def main():
    # Create a sample image (black background with colored shapes)
    img = np.zeros((400, 600, 3), dtype=np.uint8)
    
    # Draw a blue rectangle
    cv2.rectangle(img, (50, 50), (200, 150), (255, 0, 0), -1)
    
    # Draw a green circle
    cv2.circle(img, (400, 100), 50, (0, 255, 0), -1)
    
    # Draw a red ellipse
    cv2.ellipse(img, (300, 300), (100, 50), 45, 0, 360, (0, 0, 255), -1)
    
    # Add some text
    cv2.putText(img, 'OpenCV Demo', (150, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    # Save the image
    cv2.imwrite('sample_image.png', img)
    print("Image saved as 'sample_image.png'")
    
    # Load the image
    loaded_img = cv2.imread('sample_image.png')
    
    # In a headless environment, we'll skip displaying the image
    print("Running in headless environment - skipping image display")
    print("In a desktop environment, this script would display the image in a window")
    
    # Save a modified version
    cv2.putText(loaded_img, ' Modified', (150, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imwrite('sample_image_modified.png', loaded_img)
    print("Modified image saved as 'sample_image_modified.png'")
    
    # Confirm files were created
    if os.path.exists('sample_image.png'):
        print("Original image file created successfully.")
    else:
        print("Error: Original image file was not created.")
        
    if os.path.exists('sample_image_modified.png'):
        print("Modified image file created successfully.")
    else:
        print("Error: Modified image file was not created.")

if __name__ == "__main__":
    main()