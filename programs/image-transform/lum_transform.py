import cv2 
import numpy as np
import os

def transform_add(image, add_by):
    return np.clip(image + add_by, 0, 255)

def transform_mult(image, factor):
    return np.clip(image * factor, 0, 255)

def transform_log(image, c):
    lookup = np.array([np.log(i/255 + 1) * c * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, lookup)

def transform_gamma(image, gamma):
    gamma_inv = 1 / gamma
    lookup = np.array([((i / 255) ** gamma_inv) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, lookup)

mainpath = os.path.dirname(os.getcwd())
imagepath = os.path.join(mainpath, "images", "hello.jpg")

image = cv2.imread(imagepath)
image = cv2.resize(image, (image.shape[1] // 3, image.shape[0] // 3))

cv2.imshow("Original image", image)
cv2.waitKey(0)

image_add = transform_add(image, 15)
print(image_add.dtype)
cv2.imshow("Transformed image", image_add)
cv2.waitKey(0)

image_mult = transform_mult(image, 3)
print(image_mult.dtype)
cv2.imshow("Transformed image", image_mult)
cv2.waitKey(0)

image_gamma = transform_gamma(image, 0.85)
print(image_gamma.dtype)
cv2.imshow("Transformed image", image_gamma)
cv2.waitKey(0)

image_log = transform_log(image, 1.2)
print(image_log.dtype)
cv2.imshow("Transformed image", image_log)
cv2.waitKey(0)

cv2.destroyAllWindows()
