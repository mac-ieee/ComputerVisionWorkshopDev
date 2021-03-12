import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',0)
#simply canny edge detection over an image, can also change input to video
edges = cv2.Canny(img,100,200)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()