import cv2
import numpy as np


#Loads image in BGR format
image = cv2.imread("../images/hello.jpeg")
cv2.imshow("Original image", image)
cv2.waitKey(0)

print("Original image shape", image.shape)

#takes image and converts it to greyscale while loading
image_grey = cv2.imread("../images/hello.jpeg", 0)
cv2.imshow("New image", image_grey)
cv2.waitKey(0)

print("Grey image shape", image_grey.shape)

image_red = image[:, :, 2]
cv2.imshow("Image from red values", image_red)
cv2.waitKey(0)

print("Red image shape", image_red.shape)

region = cv2.selectROI("Select Region", image_grey)
print(region)

x, y, width, height = region

image_grey[y: y + height, x: x + width] = image_red[y: y + height, x: x + width]
cv2.imshow("Selected region replaced with red values!", image_grey)
cv2.waitKey(0)

replace_im = cv2.imread("../images/hello.jpg")
replace_im = cv2.resize(replace_im, (width, height))
image[y: y + height, x: x + width, :] =  replace_im
cv2.imshow("Replacing colored image roi area with another image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()