import cv2 
import numpy as np
import os

def transform_add(image, add_by):
    return np.clip(image + add_by, 0, 255)

def transform_mult(image, factor):
    return np.clip(image * factor, 0, 255)

def transform_log(image):
    pass

def transform_gamma(image, gamma):
    pass

mainpath = os.path.dirname(os.getcwd())
imagepath = os.path.join(mainpath, "images", "hello.jpg")

image = cv2.imread(imagepath)
image = cv2.resize(image, (image.shape[1] // 3, image.shape[0] // 3))

cv2.imshow("Original image", image)
cv2.waitKey(0)

image_add = transform_add(image, 50)
print(image_add.dtype)
cv2.imshow("Transformed image", image_add)
cv2.waitKey(0)

image_mult = transform_mult(image, 10)
print(image_mult.dtype)
cv2.imshow("Transformed image", image_mult)
cv2.waitKey(0)

cv2.destroyAllWindows()
