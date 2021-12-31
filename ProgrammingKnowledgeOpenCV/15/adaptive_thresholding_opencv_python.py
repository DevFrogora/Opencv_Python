import cv2

img = cv2.imread("IMG20211221121624.jpg",0)
# img = cv2.resize(img,(300,300))

img = cv2.resize(img ,(600,600))

_,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY,9,6)



while True:
    cv2.imshow("original", img)
    cv2.imshow("th1", th1)
    cv2.imshow("th2", th2)
    k = cv2.waitKey(0)
    if k == 27:
	    break

cv2.destroyAllWindows()