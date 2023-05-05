import cv2

# Load the image
image = cv2.imread('output_image.jpg')

# Define the coordinates of the region of interest (ROI)
x1, y1 = 100, 100
x2, y2 = 400, 400

# Crop the image
cropped_image = image[y1:y2, x1:x2]

# Display the original and cropped images
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
