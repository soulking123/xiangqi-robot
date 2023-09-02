import cv2
import numpy as np
# Read an image from file
image = cv2.imread('images/test_camera.jpg')
cv2.imshow('Image', image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
