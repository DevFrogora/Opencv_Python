
import cv2

cap = cv2.VideoCapture("https://25.99.135.135:8080/video");


while (cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()