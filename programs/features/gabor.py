import numpy as np
import cv2



aunty = cv2.imread("aunty.jpg")
gray_aunty = cv2.cvtColor(aunty, cv2.COLOR_BGR2GRAY)
cv2.imshow("Aunty", aunty)
cv2.waitKey(0)

for theta in np.linspace(np.pi/4, np.pi*2, 4):
    for lambda_ in np.arange(10):
        kernel = cv2.getGaborKernel((21,21), 8.0, theta, lambda_, 0.5, 0, ktype= cv2.CV_32F)

        filter_image = cv2.filter2D(gray_aunty, -1, kernel=kernel)
        cv2.imshow("Filtered image", filter_image)
        cv2.waitKey(0)
        
cv2.destroyAllWindows()

