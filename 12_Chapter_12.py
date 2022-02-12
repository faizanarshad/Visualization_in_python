# import library 

import cv2 as cv
import numpy as np


cap = cv.VideoCapture(0)

cap.set(10, 100)# 10 is the key to set the Brightness


cap.set(3, 640) #Width 1280
cap.set(4, 480) #Height 1080 for HD


while(True):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("frame",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cap.destroyAllWindows()