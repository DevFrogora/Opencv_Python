import cv2 as cv
import numpy as np

img = cv.imread( 'football_kick.jpg')
new_img = np.copy(img)

def originalState(x):
	new_img[:] =np.copy(img)

def bchannel(x):
	new_img[:, :, 0] = x

def gchannel(x):
	# new_img = img.copy()
	new_img[:, :, 1] = x

def rchannel(x):
	# new_img = img.copy()
	new_img[:, :, 2] = x



cv.namedWindow('image')
# img.copy()
cv.createTrackbar('B','image',0,255,bchannel)
cv.createTrackbar('G','image',0,255,gchannel)
cv.createTrackbar('R','image',0,255,rchannel)
switch = 'OFF--ON'
cv.createTrackbar(switch,'image',0,1,originalState)

while(1):
	cv.imshow('image',new_img)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	b= cv.getTrackbarPos('B','image')
	g = cv.getTrackbarPos('G', 'image')
	r = cv.getTrackbarPos('R', 'image')

	# img[:] =[b,g,r]

cv.destroyAllWindows()