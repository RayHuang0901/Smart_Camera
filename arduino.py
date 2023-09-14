# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 13:12:10 2023

@author: Joanne
"""

import cv2
import numpy as np
import serial

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap.open(1,cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
ser = serial.Serial('COM5', 9600)


print("error")
while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 2, 5)
    if len(faces):
        (x, y, w, h) = max(faces, key=lambda face: face[2]*face[3])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        position = x + w/2.0
        print(position)
        if position < 320:
            ser.write(b'a')
        else:
            ser.write(b'b')
        
    cv2.imshow('face', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()