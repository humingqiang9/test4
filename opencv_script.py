import cv2
import numpy as np
import uuid
import os

# Create a sample image (a blue square with a red circle)
image = np.zeros((400, 400, 3), dtype=np.uint8)
image[:] = (255, 0, 0)  # Blue background (BGR format)

# Draw a red circle
cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)

# Display the image (commented out for headless environments)
# cv2.imshow('Sample Image', image)
# print("Image displayed. Press any key to continue...")
# cv2.waitKey(0)  # Wait for a key press
# cv2.destroyAllWindows()

# Generate a random filename
random_filename = f"image_{uuid.uuid4().hex}.jpg"

# Save the image
cv2.imwrite(random_filename, image)
print(f"Image saved as {random_filename}")

# Verify the file was saved
if os.path.exists(random_filename):
    print(f"File {random_filename} successfully saved!")
else:
    print("Error saving the file.")