import cv2

# Read image
img = cv2.imread('output_image.jpg', cv2.IMREAD_ANYDEPTH)

# Get the depth of the image
depth = img.dtype

# Print the depth of the image
print(f"The depth of the image is {depth}")

# Display the image
cv2.imshow("Image", img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
