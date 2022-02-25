# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 23:00:07 2022

@author: udaya
"""

from djitellopy import Tello
import cv2
import numpy as np
 
 
def initializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff() #Turning off the streams, if any preious streams were on
    myDrone.streamon()
    return myDrone
 
def telloGetFrame(myDrone, w= 360,h=240):
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame,(w,h))
    return img
 
def findFace(img):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,6) #These parameters are scale factor and minimum neighbours, can be altered based on the accuracy.
 
    myFaceListC = [] #This stores the center faces of all the detected faces in the frame.
    myFaceListArea = [] #Respective area of faces detected rectangle
 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cx = x + w//2
        cy = y + h//2
        area = w*h
        myFaceListArea.append(area) #Appending the area to list
        myFaceListC.append([cx,cy]) #Appending centers of the detected faces
 
    if len(myFaceListArea) !=0: #Checking for prescence of face in the frame
        i = myFaceListArea.index(max(myFaceListArea)) #Finding the largest area of the face index, that gives the closest face details
        return img, [myFaceListC[i],myFaceListArea[i]] #Returning the image, area at index i, 
    else:
        return img,[[0,0],0]
 
def trackFace(myDrone,info,w,pid,pError):
 
    ## PID
    error = info[0][0] - w//2 #Error = cx - width of frame/2
    #PID is used for smooth transition of speeds, and hence PID dives the speed of drone using kp*error + kd*(error - pError), here we are not using ki
    speed = pid[0]*error + pid[1]*(error-pError)
    # The abve function may yield bigger values so limiting the value using numpy clip method.
    speed = int(np.clip(speed,-100,100))
 
 
    print(speed)
    if info[0][0] !=0:
        myDrone.yaw_velocity = speed
    else:
        myDrone.for_back_velocity = 0
        myDrone.left_right_velocity = 0
        myDrone.up_down_velocity = 0
        myDrone.yaw_velocity = 0
        error = 0
    if myDrone.send_rc_control: #Sending back the updated velocities to drone for maneavur
        myDrone.send_rc_control(myDrone.left_right_velocity,
                                myDrone.for_back_velocity,
                                myDrone.up_down_velocity,
                                myDrone.yaw_velocity)
    return error