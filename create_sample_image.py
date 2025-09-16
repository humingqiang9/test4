import cv2
import numpy as np

# Create a sample image (black background with a white rectangle)
img = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.rectangle(img, (50, 50), (250, 250), (255, 255, 255), -1)

# Save the sample image
cv2.imwrite('sample_image.jpg', img)
print("Sample image created: sample_image.jpg")