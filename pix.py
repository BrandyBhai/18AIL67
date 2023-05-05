import cv2

# Read image
img = cv2.imread('output_image.jpg')

# Get the dimensions of the image
height, width, channels = img.shape

# Loop through each pixel and display its RGB values
for i in range(height):
    for j in range(width):
        b, g, r = img[i,j]
        print(f"Pixel ({i}, {j}): R = {r}, G = {g}, B = {b}")

# Display the image
cv2.imshow("Image", img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
