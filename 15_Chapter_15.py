# Resolution of cam

import cv2 as cv
import numpy as np
from tblib import Frame

#
cap = cv.VideoCapture(0)
#Resolution
#cap.set(3,1280)
#cap.set(4,720)

def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)
def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
# how to change and fix the frame 30fph
#hd_resolution()
#sd_resolution()
fhd_resolution
while(True):
    ret,frame = cap.read()
    if ret == True:
        cv.imshow("camera",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()