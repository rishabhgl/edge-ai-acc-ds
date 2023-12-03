import cv2
import numpy as np

city = cv2.imread("city.jpeg")
city = cv2.resize(city, (city.shape[1] * 2, city.shape[0] * 2))
cv2.imshow("City", city)
cv2.waitKey(0)

city_gray = cv2.cvtColor(city, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(city_gray, None)
city_kp = cv2.drawKeypoints(city_gray, keypoints, city)
cv2.imshow("city", city_kp)
cv2.waitKey(0)
cv2.destroyAllWindows()

orb = cv2.ORB_create()
keypoints, descriptors = orb.detectAndCompute(city_gray, None)
city_new = cv2.drawKeypoints(city_gray, keypoints, city)
cv2.imshow("city", city_new)
cv2.waitKey(0)
cv2.destroyAllWindows()