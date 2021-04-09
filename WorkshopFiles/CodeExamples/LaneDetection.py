import cv2
import numpy as np
import matplotlib.pyplot as plt

#canny detection
def canny(image):
	#2 convert image to grayscale
	gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
	#3 reduce noise
	blur = cv2.GaussianBlur(gray, (5,5), 0)
	#canny
	canny = cv2.Canny(blur, 50, 150)
	return canny

#5 isolate lane lines
def region_of_interest(image):
	height = image.shape[0]
	polygons = np.array([
	[(0, height), (1280, height), (642, 284)]
	])
	mask = np.zeros_like(image)
	cv2.fillPoly(mask, polygons, 255)
	#6 bitwise and
	masked_image = cv2.bitwise_and(image, mask)
	return masked_image

#shows lane lines on masked image
def display_lines(image, lines):
	line_image = np.zeros_like(image)
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.reshape(4)
			cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
	return line_image

#1 read image
image = cv2.imread("test_laneImage.jpg") 
lane_image = np.copy(image)

#4 apply edge detection canny
canny_image = canny(lane_image)
masked_image = region_of_interest(canny_image)

#7 finding lane lines using hough transform 
lines = cv2.HoughLinesP(masked_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
line_image = display_lines(lane_image, lines)
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

cv2.imshow(combo_image)
cv2.waitKey(0)