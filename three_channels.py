import cv2
import numpy as np
# Read image
img = cv2.imread('output_image.jpg')

# Split the image into its RGB channels
b, g, r = cv2.split(img)

# Convert the BGR image to RGB format
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create images for the red, green, and blue channels
r_img = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])
g_img = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
b_img = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])

# Display the red, green, and blue channels as separate images
cv2.imshow("Red Channel", r_img)
cv2.imshow("Green Channel", g_img)
cv2.imshow("Blue Channel", b_img)

# Display the original image
cv2.imshow("Original Image", img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
