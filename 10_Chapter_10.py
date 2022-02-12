#Convert the webcamvideo into the different frames

import cv2 as cv


# load a video into the code with webcam
cap = cv.VideoCapture(0)


while (True):
    (ret,frame) =  cap.read()# read the video and convert into the frame
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert the video ito graycolor
    (thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the Binary
    # To Show in Player updated
    if ret == True:
        #out.write(grayframe)
        cv.imshow('Original',frame) # Original image taken from webcam
        cv.imshow("Gray",grayframe) # Gray image after the conversion
        cv.imshow('Black_white',binaryimg) #convert the webcam image into the Black and White Image
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
cv.destroyAllWindows()