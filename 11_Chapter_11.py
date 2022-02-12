# writing videos from cam

import cv2 as cv
import numpy as np

# load a video into the code with webcam
cap = cv.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resourses/cam_vedio.avi',cv.VideoWriter_fourcc('M',"j",'P','G'),10,(frame_width,frame_height),isColor=False)


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