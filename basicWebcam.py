import numpy as np
import cv2
#if you have multiple cameras change the number to see which one it selects
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    #checks for esc keypress to to stop running
    if cv2.waitKey(1) & 0xFF == 27:
        break
    #if press s will save the image to a file called save.jpg
    elif cv2.waitKey(1) == ord('s'):
        cv2.imwrite('test.jpg', frame)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
