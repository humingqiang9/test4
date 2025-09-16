import cv2
import numpy as np
import uuid
import os

# Create a sample image (black image with a white rectangle and text)
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw a white rectangle
cv2.rectangle(image, (50, 50), (550, 350), (255, 255, 255), -1)

# Add some text
cv2.putText(image, 'OpenCV Example', (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)

# Generate a random filename
random_filename = str(uuid.uuid4()) + '.jpg'

# Save the image
cv2.imwrite(random_filename, image)

print(f"Image saved as {random_filename}")