import cv2 as cv
import numpy as np

def nothing(x):
	pass

def fixHSVRange(h, s, v):
    # Normal H,S,V: (0-360,0-100%,0-100%)
    # OpenCV H,S,V: (0-180,0-255 ,0-255)
    return (180 * h / 360, 255 * s / 100, 255 * v / 100)

cap = cv.VideoCapture("VID20211220153637.mp4");


cv.namedWindow('Tracking')
cv.createTrackbar('LH','Tracking',0,255,nothing)
cv.createTrackbar('LS','Tracking',0,255,nothing)
cv.createTrackbar('LV','Tracking',0,255,nothing)
cv.createTrackbar('UH','Tracking',255,255,nothing)
cv.createTrackbar('US','Tracking',255,255,nothing)
cv.createTrackbar('UV','Tracking',255,255,nothing)

fourcc = cv.VideoWriter_fourcc(*'mp4v')
# fourcc =  0x7634706d
print(cap.get(cv.CAP_PROP_FRAME_WIDTH) , cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# frame size pass it as height , width
out= cv.VideoWriter('output.mp4',fourcc,30,(720, 1280))
while(1):

    _,frame = cap.read()
    # print(frame.shape)
    # frame = cv.imread('IMG20211220141059.jpg')
    if frame is  None :
        break
    else:
        # frame = cv.resize(frame,(500,500))

        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        l_h = cv.getTrackbarPos('LH','Tracking')
        l_s = cv.getTrackbarPos('LS','Tracking')
        l_v = cv.getTrackbarPos('LV','Tracking')

        u_h = cv.getTrackbarPos('UH','Tracking')
        u_s = cv.getTrackbarPos('US','Tracking')
        u_v = cv.getTrackbarPos('UV','Tracking')


        l_b = np.array([l_h,l_s,l_v])
        u_b = np.array([u_h, u_s, u_v])

        # https: // stackoverflow.com / questions / 36817133 / identifying - the - range - of - a - color - in -hsv - using - opencv
        # blue
        # [95 121 113][156 255 255]
        l_b=np.array([95,121, 113])
        u_b =np.array([156, 255, 255])
        print(l_b, u_b)
        blue_mask = cv.inRange(hsv ,l_b,u_b)

        blue_res = cv.bitwise_and(frame,frame,mask=blue_mask)

        # red
        # 'red1': [[180, 255, 255], [159, 50, 70]],
        # 'red2': [[9, 255, 255], [0, 50, 70]],
        rl_b=np.array([159, 50, 70])
        ru_b =np.array([180, 255, 255])

        red_mask = cv.inRange(hsv, rl_b, ru_b)
        red_res = cv.bitwise_and(frame, frame, mask=red_mask)

        res = cv.add(blue_res, red_res)
        # 'white': [[180, 18, 255], [0, 0, 231]],
        #[101  31 231] [255 255 255]

        wl_b=np.array([101 , 31 ,231])
        wu_b =np.array([255,255,255])

        white_mask = cv.inRange(hsv, wl_b, wu_b)
        white_res = cv.bitwise_and(frame, frame, mask=white_mask)
        res = cv.add(res, white_res)

        # black
        # [5 ,0, 0][186,255,95]
        black_l_b=np.array([5, 0 ,0])
        black_u_b =np.array([186,255,95])

        black_mask = cv.inRange(hsv, black_l_b, black_u_b)
        black_res = cv.bitwise_and(frame, frame, mask=black_mask)

        res = cv.add(res,black_res)


        out.write(res)

        cv.imshow('frame', frame)
        cv.imshow('mask', black_mask)
        cv.imshow('res', res)

        k = cv.waitKey(1)
        if k == 27:
            break

cap.release()
out.release()
cv.destroyAllWindows()