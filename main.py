# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:58:23 2018

@author: fd
"""

import math
import numpy as np
import cv2 
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageEnhance
import time
img=np.array(cv2.imread("1.jpg"),dtype="float64")
x0,y0,_=img.shape
x,y,_=img.shape
#blur1 = cv2.GaussianBlur(img,(13,13),0)
blur1=cv2.blur(img,(4,4))
high1=img-blur1
blur1 = cv2.resize(blur1,(int(y/2),int(x/2)))
blur1=cv2.blur(blur1,(4,4))


x,y,_=blur1.shape
blur2=cv2.GaussianBlur(blur1,(3,3),0)
high2=blur1-blur2
#blur2 = cv2.resize(blur2,(int(y/2),int(x/2)))
blur2=cv2.blur(blur2,(3,3))

x,y,_=blur2.shape
blur3=cv2.GaussianBlur(blur2,(7,7),0)
high3=blur2-blur3
#blur3 = cv2.resize(blur3,(int(y/2),int(x/2)))
#blur3=cv2.blur(blur3,(3,3))

#blur3=cv2.medianBlur(np.array(blur3,dtype="uint8"),3)
#low=cv2.medianBlur(blur,5)
#cv2.imshow("a",cv2.medianBlur(blur3,7)+cv2.medianBlur(high2,5)+high1+cv2.medianBlur(high2,3))
#cv2.imshow('blur3',blur3)
#cv2.imshow('high3',high3)
#cv2.imshow('high2',high2)
re=(cv2.resize(blur3,(y0,x0))+
           cv2.resize(high3,(y0,x0))+
           cv2.resize(high2,(y0,x0))+high1)
re=(re-np.min(re))/(np.max(re)-np.min(re))*255
cv2.imshow('result',np.array(re,dtype="uint8"))
cv2.imshow('origin',np.array(img,dtype="uint8"))
cv2.imshow('high',np.array(high1,dtype="uint8"))
cv2.imshow('low',np.array(cv2.resize(blur3,(y0,x0)),dtype="uint8"))
cv2.imshow('medium',np.array( cv2.resize(high3,(y0,x0)),dtype="uint8"))
cv2.waitKey(0)