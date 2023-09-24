import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

mainpath = os.path.dirname(os.getcwd())
image_tilt_path = os.path.join(mainpath, "images", "image2.jpg")
image_strt_path = os.path.join(mainpath, "images", "image1.jpg")

image_tilt = cv2.imread(image_tilt_path)
image_tilt_RGB = cv2.cvtColor(image_tilt, cv2.COLOR_BGR2RGB)

image_strt = cv2.imread(image_strt_path)
image_strt_RGB = cv2.cvtColor(image_strt, cv2.COLOR_BGR2RGB)

plt.imshow(image_tilt_RGB)
tilt_ref = np.float32(plt.ginput(4))
print(tilt_ref)

plt.imshow(image_strt_RGB)
strt_ref = np.float32(plt.ginput(4))
print(strt_ref)

transform = cv2.getPerspectiveTransform(tilt_ref, strt_ref)
straightened = cv2.warpPerspective(image_tilt_RGB, transform, (image_strt.shape[1], image_strt.shape[0]))


plt.subplot(121)
plt.imshow(image_tilt_RGB)
plt.title('Tilted image')

plt.subplot(122)
plt.imshow(straightened)
plt.title('Straighened Image')

plt.show()
