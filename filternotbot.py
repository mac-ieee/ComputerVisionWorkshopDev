import cv2

arg = 'edge'
image = cv2.imread('image.jpg')

filename = 'filtered.jpg'

if arg == 'blur':
	blurred = cv2.GaussianBlur(image,(33,33,),0)
	# blurred = cv2.medianBlur(image,55)
	cv2.imwrite(filename,blurred)

elif arg == 'gray':
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite(filename,gray)


elif arg == 'edge':
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray,(5,5,),0)
	edged = cv2.Canny(blurred,85,85)
	cv2.imwrite(filename,edged)

elif arg == 'reflect':
	flip = cv2.flip(image, 1)
	cv2.imwrite(filename,flip)


elif arg == 'bright':
	array = np.array([[0.01, 0.54, 0.9],[0.4, 0.01, 0.4],[0.01, 0.2, 0.01]])
	bright = cv2.filter2D(image, -1, array)
	cv2.imwrite(filename,bright)


elif arg == '70s':
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	cv2.imwrite(filename,gray)

