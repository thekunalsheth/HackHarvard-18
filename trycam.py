import numpy as np
import cv2
import time

#import the cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def TakeSnapshotAndSave():
    # access the webcam (every webcam has a number, the default is 0)
    cam = cv2.VideoCapture(0)
    
    xframe = None
    yframe = None
    wframe = None
    hframe = None
    while(True):
        # Capture frame-by-frame
        ret, frame = cam.read()
        
        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x-2,y-80),(x+w+30,y+h+100),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            xframe = x
            yframe = y
            wframe = w
            hframe = h

        textx = 0
        texty = 20
        text_color = (0,255,0)
        # write on the live stream video
        cv2.putText(frame, "Press q when ready", (textx,texty), cv2.FONT_HERSHEY_PLAIN, 1.0, text_color, thickness=2)
        
        
        # if you want to convert it to gray uncomment and display gray not fame
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Display the resulting frame
        cv2.imshow('frame',frame)
        # press the letter "q" to save the picture
#        if cv2.waitKey(1) & 0xFF == ord('q'):
        if (xframe and yframe and wframe and hframe):
            cv2.imwrite('try.jpg',frame)
            img = cv2.imread('try.jpg')
            crop_img = img[y-70:y+h+70, x:x+w+10]
            cv2.imwrite('cropped.jpg', crop_img)
            break

# When everything done, release the capture
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    TakeSnapshotAndSave()
