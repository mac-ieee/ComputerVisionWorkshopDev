import numpy as np
import cv2
#if you have multiple cameras change the number to see which one it selects
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    face_cascade = cv2.CascadeClassifier('cas4.xml')
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    #checks for esc keypress to to stop running
    if cv2.waitKey(1) & 0xFF == 27:
        break
    #if press s will save the image to a file called save.jpg
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('save.jpg', frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
