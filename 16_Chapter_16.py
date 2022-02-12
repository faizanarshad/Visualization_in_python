#saving hd cam vedio Recording
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
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resourses/hd_cam_vedio.avi',cv.VideoWriter_fourcc('M',"J",'P','G'),10,(frame_width,frame_height))


while (True):
    (ret,frame) =  cap.read()# read the video and convert into the frame
    #grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert the video ito graycolor
    #(thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the Binary
    # To Show in Player updated
    if ret == True:
        out.write(frame)
        cv.imshow('Video',frame) # Original image taken from webcam
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 


cap.release()
cv.destroyAllWindows()