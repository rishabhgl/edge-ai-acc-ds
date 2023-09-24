import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

mainpath = os.path.dirname(os.getcwd())
image1path = os.path.join(mainpath, "images", "hello1.jpeg")
image2path = os.path.join(mainpath, "images", "hello.jpg")

image = cv2.imread(image1path)
replace_image = cv2.imread(image2path)

image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
replace_image_RGB = cv2.cvtColor(replace_image, cv2.COLOR_BGR2RGB)

plt.imshow(replace_image_RGB)
pt = np.int32(plt.ginput(1))
x, y = pt[0]
height, width, _ = image_RGB.shape 
print(x, y)

replace_image_RGB[y: y + height, x: x + width, :] = image_RGB[:, :, :]
plt.imshow(replace_image_RGB)
plt.show()
