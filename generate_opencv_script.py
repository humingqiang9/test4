import cv2
import uuid

# Generate a random filename
random_filename = str(uuid.uuid4())[:8] + ".py"
print(f"Script will be saved as: {random_filename}")

# The actual script content
script_content = '''import cv2

# Load an image from file
img = cv2.imread('sample_image.jpg')

# Check if image was loaded successfully
if img is None:
    print("Error: Could not load image. Please check the file path.")
else:
    # Display the image
    cv2.imshow('Loaded Image', img)
    
    # Wait for a key press and then close the window
    print("Press any key to close the image window...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Save the image with a new name
    cv2.imwrite('processed_image.jpg', img)
    print("Image saved as processed_image.jpg")
'''

# Save the script to a file with the random name
with open(random_filename, 'w') as f:
    f.write(script_content)

print(f"Python script has been created and saved as {random_filename}")