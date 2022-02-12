# Assighnment
#Import Library
import numpy as np #numpy for array
import cv2 as cv    #cv2 for openCV

cap = cv.VideoCapture(0)    #activate the WebCam
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# Define the codec and create VideoWriter object
out = cv.VideoWriter('resourses/cam_out_vedio1.avi',cv.VideoWriter_fourcc('M',"J",'P','G'),10,(frame_width,frame_height))

while cap.isOpened():
    ret, frame = cap.read() # Read the webcam convert it into frames
     
    # write the flipped frame
    out.write(frame)    #save the frame or video
    cv.imshow('frame', frame) #Image show 
    if cv.waitKey(1) == ord('q'): # wait key it will not let the disparse ina second
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()