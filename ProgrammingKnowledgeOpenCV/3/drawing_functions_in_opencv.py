import cv2

img = cv2.imread(  'human.png',-1)

img = cv2.line(img, (0,0),(255,255) ,(255,0,0), 5)
img = cv2.arrowedLine(img, (0,255),(255,255) ,(255,0,0), 5)

img = cv2.rectangle(img, (250,0),(500,250) ,(0,0,255), 10)
img = cv2.circle(img, (370,125),125 ,(0,255,0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX

img= cv2.putText(img,'OpenCv' ,(10,450),font,4,(0,255,255),10,cv2.LINE_AA)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('human_copy.png',img)
	cv2.destroyAllWindows()