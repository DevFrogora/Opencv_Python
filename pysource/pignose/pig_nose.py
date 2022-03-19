import cv2
import numpy as np
import dlib
from math import hypot



cap = cv2.VideoCapture(0)
nose_image = cv2.imread("pig-nose.png")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("E:\Tutorial\PycharmProjects\pythonProject\pysource\Eye Detection\shape_predictor_68_face_landmarks.dat")

def midpoint(p1,p2):
    return int((p1.x +p2.x)/2) ,int((p1.y +p2.y)/2)


while True:
    success , frame = cap.read()
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = detector(gray_frame)
    if faces:
        for face in faces:
            landMarks = predictor(gray_frame, face)

            top_point = (landMarks.part(29).x, landMarks.part(29).y)
            center_point = (landMarks.part(30).x, landMarks.part(30).y)
            left_point = (landMarks.part(31).x, landMarks.part(31).y)
            right_point = (landMarks.part(35).x, landMarks.part(35).y)
            left_right_mid_nose = midpoint(landMarks.part(31),landMarks.part(35))

            nose_width = int(hypot(left_point[0] -right_point[0],
                               left_point[1]-right_point[1])+15)

            nose_height= int(hypot(left_right_mid_nose[0] - top_point[0],
                               left_right_mid_nose[1] - top_point[1])+15)

            # print(nose_width,nose_height)
            top_left = (int(center_point[0] - nose_width/2) ,
                                 int(center_point[1] - nose_height/2))

            bottom_right = (int(center_point[0] + nose_width / 2),
                           int(center_point[1] + nose_height / 2))
            # cv2.rectangle(frame,top_left,bottom_right,
            #               (0,255,0) ,2)

            nose_pig = cv2.resize(nose_image,(nose_width,nose_height))
            nose_pig_gray = cv2.cvtColor(nose_pig,cv2.COLOR_BGR2GRAY)
            _ , nose_mask = cv2.threshold(nose_pig_gray,25,255,cv2.THRESH_BINARY_INV)

            nose_area = frame[top_left[1]:top_left[1]+nose_height,
                        top_left[0]: top_left[0]+nose_width]

            nose_area_no_nose = cv2.bitwise_and(nose_area,nose_area,mask= nose_mask)
            final_nose= cv2.add(nose_area_no_nose,nose_pig)

            frame[top_left[1]:top_left[1] + nose_height,
            top_left[0]: top_left[0] + nose_width] = final_nose
            # cv2.imshow("nose_area", nose_area)
            # cv2.imshow("nose_pig", nose_pig)
            # cv2.imshow("nose_mask", nose_mask)
            # cv2.imshow("nose_area_no_nose", nose_area_no_nose)
            # cv2.imshow("final_nose", final_nose)


    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()