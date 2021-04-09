import cv2
import numpy as np

cars_cascade = cv2.CascadeClassifier("car_detection.xml")
img = cv2.imread('truck.jpg')
img1 = cv2.resize(img,(600,450)) #resize the image accordingly - preferably close to the scale of the original img
# Note: (when images are too big detection fails)

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #convert to grayscale

#For img 1
#cars = cars_cascade.detectMultiScale(gray, 1.1, 3, minSize=(250,250))
cars = cars_cascade.detectMultiScale(gray, 1.1, 3, minSize=(200,200))
#minsize should be indicated for better detection (also can be adjusted accordingly if detection fails)

for (x, y, w, h) in cars:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (255,0,0),5)

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()