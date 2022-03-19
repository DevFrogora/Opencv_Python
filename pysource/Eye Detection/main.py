import cv2
import numpy as np
import dlib



cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def midpoint(p1,p2):
    return int((p1.x +p2.x)/2) ,int((p1.y +p2.y)/2)

while True:
    success , frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    if faces:
        for face in faces:
            # x,y = face.left(), face.top()
            # x1,y1 = face.right(),  face.bottom()
            # cv2.rectangle(frame ,(x,y),(x1,y1),(0,200,0),2)
            landMarks = predictor(gray, face)
            left_point = (landMarks.part(36).x ,landMarks.part(36).y)
            right_point = (landMarks.part(39).x,landMarks.part(39).y)
            center_top = midpoint(landMarks.part(37),landMarks.part(38))
            center_buttom = midpoint(landMarks.part(41),landMarks.part(40))

            # cv2.circle(frame,(x,y),3,(0,0,255),2)
            hor_line = cv2.line(frame,left_point,right_point,(0,255,0),2)
            ver_line = cv2.line(frame, center_top, center_buttom, (0, 255, 0), 2)

    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()