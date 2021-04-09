import numpy as np
import cv2 as cv

#loading an image have two options can load as greyscale or coloured
#can change name of file but make sure the file is in the same folder
img = cv.imread('test.jpg')
b,g,r = cv.split(img)

#Displaying an image by having a window and closing when any button is pressed

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',r)
cv.waitKey(0)
cv.destroyAllWindows()