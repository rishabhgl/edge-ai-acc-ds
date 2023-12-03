import cv2 
import numpy as np
import os

mainpath = os.path.dirname(os.getcwd())
detector_path = os.path.join(mainpath, "utils", "haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier(detector_path)

while True:
    _, frame = camera.read()
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(frame_grey, scaleFactor= 1.1, minNeighbors= 9)

    for x, y, width, height in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), color= (0, 0, 0), thickness= 2)

    cv2.imshow("Frame seen", frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()