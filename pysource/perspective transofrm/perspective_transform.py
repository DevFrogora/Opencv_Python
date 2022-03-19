import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_,frame = cap.read()
cv2.imshow("Frame", frame)
print(frame.shape)
clickedpts= []
pagePts = np.float32([[274,478],[574,189],[274,478],[600,478]])
pts2 = np.float32([[0,0],[480,0],[0,640],[480,640]])



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x, ' , ', y)

        # text = 'x: ' + str(x) + ' y: ' + str(y)
        clickedpts.append([x,y])
        # cv2.imshow('Frame', frame)

        # x , y = clickedpts[0]

cv2.setMouseCallback('Frame', click_event)



def overlayThePointOnScreen(clickedpts ,frame):
    # if clickedpts:
        for pts in clickedpts:
            x,y = pts
            # text = (  " x==" + str(x) + " y==" + str(y))
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(frame, text, (x, y), font, .5, (255, 255, 0), 2, cv2.LINE_AA)
            # print((clickedpts))
            # cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

while True:
    success , frame = cap.read()

    pagePts = ([[297, 191], [574, 189], [274, 478], [600, 478]])
    pts2 = ([[0, 0], [480, 0], [0, 640], [480, 640]])
    # / np.float32
    print(pagePts[0])
    cv2.circle(frame, pagePts[0], 5, (0, 0, 255), -1)
    cv2.circle(frame, pagePts[1], 5, (0, 0, 255), -1)
    cv2.circle(frame, pagePts[2], 5, (0, 0, 255), -1)
    cv2.circle(frame, pagePts[3], 5, (0, 0, 255), -1)

    matrix = cv2.getPerspectiveTransform(np.float32(pagePts), np.float32(pts2))
    result = cv2.warpPerspective(frame,matrix,(480,640))
    # overlayThePointOnScreen(pagePts,frame)


    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective Transform", result)
    key = cv2.waitKey(1)
    if key == 27:
        break



cap.release()
cv2.destroyAllWindows()
















# cv2.setMouseCallback('image', click_event)