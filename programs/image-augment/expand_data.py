import cv2
import numpy as np
import os
import imutils

mainpath = os.path.dirname(os.getcwd())
imagepath = os.path.join(mainpath, "images", "hello.jpg")

image = cv2.imread(imagepath)
height, width, _ = image.shape
image = cv2.resize(image, (width // 3, height // 3))
cv2.imshow("Image", image)
cv2.waitKey(0)

for alpha in np.linspace(0.1, 2.1, 10, endpoint= False):
    alpha = np.around(alpha, decimals= 2)
    brightened = cv2.convertScaleAbs(image, alpha = alpha, beta= 1)
    cv2.imshow("Bright" + str(alpha), brightened)
    cv2.waitKey(0)
    for angle in range(-90, 90, 30):
        transformed = imutils.rotate_bound(brightened, angle)
        filepath = os.path.join(os.getcwd(), "dataset\\")
        filepath = filepath + "alpha_" + str(alpha) + "_angle_" + str(angle) + ".jpg"
        print(filepath)
        cv2.imwrite(filepath, transformed)
        