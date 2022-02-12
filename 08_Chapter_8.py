# converting a vedio into Gray and Black and white

#import a library 
import cv2 as cv


# load a video into the code
cap = cv.VideoCapture('resourses/video.mkv')
# writing format ,codec,video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter('resourses/out_vedio.avi',cv.VideoWriter_fourcc('M',"J",'P','G'),10,(frame_width,frame_height),isColor= False)

while (True):
    (ret,frame) =  cap.read()# read the video and convert into the frame
    grayframe = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#convert the video ito graycolor
    #(thresh,binaryimg) = cv.threshold(grayframe,127,255,cv.THRESH_BINARY)#convert he video into the black
    # To Show in Player
    if ret == True:
        out.write(grayframe)
        cv.imshow("vedio",grayframe)
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
out.release()
cv.destroyAllWindows()