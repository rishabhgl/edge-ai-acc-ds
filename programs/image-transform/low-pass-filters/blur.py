import cv2
from PIL import Image, ImageFilter
import numpy as np
import os

mainpath = os.path.dirname(os.getcwd())
imagepath = os.path.join(mainpath, "images","hello.jpeg")

image = cv2.imread(imagepath)
pil_image = Image.open(imagepath)
cv2.imshow("Image", image)
cv2.waitKey(0)

size = 5
#Mean Filter
blur_image = cv2.blur(image, (size, size))
cv2.imshow("Blurred Image", blur_image)
cv2.waitKey(0)

max_image = pil_image.filter(ImageFilter.MaxFilter(size= size))
max_image.show()

min_image = pil_image.filter(ImageFilter.MinFilter(size= size))
min_image.show()

median_image = pil_image.filter(ImageFilter.MedianFilter(size= size))
median_image.show()

cv2.destroyAllWindows()

