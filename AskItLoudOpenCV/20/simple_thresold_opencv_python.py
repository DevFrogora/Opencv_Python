import cv2

img = cv2.imread("black_white.png",0)
# img = cv2.resize(img,(300,300))


_,th1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,250,255,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,180,255,cv2.THRESH_TOZERO_INV)


while True:
    cv2.imshow("original", img)
    cv2.imshow("th1", th1)
    cv2.imshow("th2", th2)
    cv2.imshow("th3", th3)
    cv2.imshow("th4", th4)
    cv2.imshow("th5", th5)
    k = cv2.waitKey(0)
    if k == 27:
	    break

cv2.destroyAllWindows()