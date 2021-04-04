import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def lanesDetection(img, image_index):

    height = img.shape[0]
    width = img.shape[1]

    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray_img, (5,5), 0)
    edge = cv.Canny(blur, 50, 150)

    #if running on image, use this region of interest
    if image_index == 1:
        cropped_image = region_of_interest_image(edge)
    #if running on video, use this region of interest
    else:
        region_of_interest_vertices = [(200, height), (width/2, height/1.37), (width-300, height)]
        cropped_image = region_of_interest(
            edge, np.array([region_of_interest_vertices], np.int32))

    lines = cv.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

    line_image = display_lines(img, lines)
    image_with_lines = cv.addWeighted(img, 0.8, line_image, 1, 1)

    return image_with_lines

#region of interest for an image
def region_of_interest_image(image):
	height = image.shape[0]
	polygons = np.array([
	[(0, height), (1280, height), (642, 284)]
	])
	mask = np.zeros_like(image)
	cv.fillPoly(mask, polygons, 255)
	#6 bitwise and
	masked_image = cv.bitwise_and(image, mask)
	return masked_image

#region of interest for a video
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = (255)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

#shows lane lines on masked image
def display_lines(image, lines):
	line_image = np.zeros_like(image)
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line.reshape(4)
			cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
	return line_image

def videoLanes():
    cap = cv.VideoCapture('./img/Lane.mp4')
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = lanesDetection(frame, 0)
        cv.imshow('Lanes Detection', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    #running on image
    # image = cv.imread('./img/test_image2.png') 
    # lane_image = np.copy(image)
    # frame = lanesDetection(lane_image, 1)
    # cv.imshow('Lanes Detection', frame)
    # cv.waitKey(0)

    #running on video
    videoLanes()