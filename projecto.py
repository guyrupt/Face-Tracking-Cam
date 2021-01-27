#!/usr/bin/env python
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

cap = cv2.VideoCapture(0)
_, frame=cap.read()
rows,cols,_=frame.shape
center = int(cols/2)
deg=90
x_m=90
count=0 
face_cascade = cv2.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalcatface.xml')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
servo1.start(0)
while True:
    _, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,2)
    count+=1
    for (x,y,w,h) in faces:
        x_m=int((x+x+w)/2)
        cv2.line(frame,(x_m,0),(x_m,480),(0,255,0),2)
        count=0
        print("detected")
        
        
    
   
    cv2.imshow("Frame",frame)
    
    key=cv2.waitKey(1)
    
    if key==113:
        break
    if x_m<center-15:
        deg += 5
        if count == 3:
            deg -= 15
            count=0
    elif x_m>center+15:
        deg -= 5
        if count == 3:
            deg += 15
            count=0
    if deg >= 180:
        deg=165
    if deg <= 0:
        deg=15
        
    
        
    
    
    servo1.ChangeDutyCycle(2+(deg/18))
    time.sleep(0.2)
    servo1.ChangeDutyCycle(0)
    
    

print('quit successfully')
servo1.ChangeDutyCycle(2+(90/18))
time.sleep(0.015)
servo1.ChangeDutyCycle(0)
servo1.stop()
GPIO.cleanup()
cv2.destroyAllWindows()  
cap.release()
