import cv2
import numpy as np

# Read image
img = cv2.imread('output_image.jpg')
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grayscale_image = grayscale(img)
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", grayscale_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()