import cv2 as cv
import numpy as np

def nothing(x):
	pass

def fixHSVRange(h, s, v):
    # Normal H,S,V: (0-360,0-100%,0-100%)
    # OpenCV H,S,V: (0-180,0-255 ,0-255)
    return (180 * h / 360, 255 * s / 100, 255 * v / 100)



cv.namedWindow('Tracking')
cv.createTrackbar('LH','Tracking',0,255,nothing)
cv.createTrackbar('LS','Tracking',0,255,nothing)
cv.createTrackbar('LV','Tracking',0,255,nothing)
cv.createTrackbar('UH','Tracking',255,255,nothing)
cv.createTrackbar('US','Tracking',255,255,nothing)
cv.createTrackbar('UV','Tracking',255,255,nothing)


while(1):


    # print(frame.shape)
    frame = cv.imread('IMG20211220141059.jpg')
    if frame is  None :
        break
    else:
        frame = cv.resize(frame,(500,500))

        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        l_h = cv.getTrackbarPos('LH','Tracking')
        l_s = cv.getTrackbarPos('LS','Tracking')
        l_v = cv.getTrackbarPos('LV','Tracking')

        u_h = cv.getTrackbarPos('UH','Tracking')
        u_s = cv.getTrackbarPos('US','Tracking')
        u_v = cv.getTrackbarPos('UV','Tracking')


        l_b = np.array([l_h,l_s,l_v])
        u_b = np.array([u_h, u_s, u_v])


        print(l_b, u_b)
        mask = cv.inRange(hsv ,l_b,u_b)

        res = cv.bitwise_and(frame,frame,mask=mask)


        cv.imshow('frame', frame)
        cv.imshow('mask', mask)
        cv.imshow('res', res)

        k = cv.waitKey(1)
        if k == 27:
            break

cv.destroyAllWindows()