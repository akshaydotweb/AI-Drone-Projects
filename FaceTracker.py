import cv2
import numpy as np

def findFace(img):
    faceCascade = cv2.CascadeClassifier("Resources/haarcascades/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceList= []
    myFaceListArea = []

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cx = x + w//2
        cy = y + h//2
        area = w * h
        myFaceList.append([cx, cy])
        myFaceListArea.append(area)
        cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        cap = cv2.VideoCapture(0)

    while True:
        _, img = cap.read()
        findFace(img)
        cv2.imshow("Output", img)
        cv2.waitKey(1)
