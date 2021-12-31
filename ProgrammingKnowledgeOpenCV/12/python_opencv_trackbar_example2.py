import cv2 as cv
import numpy as np

def nothing(x):
	print(x)



cv.namedWindow('image')
# img.copy()
cv.createTrackbar('COUNT','image',0,255,nothing)
switch = 'color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
	img = cv.imread('football_kick.jpg')
	font = cv.FONT_HERSHEY_SIMPLEX
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	b= cv.getTrackbarPos('COUNT','image')
	s= cv.getTrackbarPos(switch,'image')
	cv.putText(img, str(b), (50, 150), font, 2, (0, 0, 255))

	if s == 0:
		pass
	else:
		img=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	cv.imshow('image', img)

	# img[:] =[b,g,r]

cv.destroyAllWindows()