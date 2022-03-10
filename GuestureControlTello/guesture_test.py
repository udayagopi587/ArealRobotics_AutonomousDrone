# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 18:18:52 2022

@author: udaya
"""

from gesture_recognition import GestureRecognition , GestureBuffer 
import cv2
from time import sleep
import numpy as np

fontScale              = 1
fontColor              = (255,255,255)
thickness              = 1
lineType               = 2

gesturemodel  =  GestureRecognition()
gesturebuffer = GestureBuffer()
cap = cv2.VideoCapture(0)

while True:
    ok, img = cap.read()
    img = cv2.resize(img,(640, 480))
    debug_image, gesture_id = gesturemodel.recognize(img)
    gesturebuffer.add_gesture(gesture_id)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    cv2.imshow("GuestureDisplay",debug_image)
cv2.destroyAllWindows()