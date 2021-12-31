import numpy as np
import cv2

img = cv2.imread('football_kick.jpg')

print(img.shape) #return a tuple of number of rows, columns and channels
print(img.size) #return Total numbber of pixels is accessed
print(img.dtype) #return Image datatype as obtained

(b,g,r) = cv2.split(img)
img = cv2.merge((b, g, r))

# 305  ,  170
# 353  ,  215
x1=305
x2=353
y1=170
y2=215
ball_roi = img[y1:y2, x1:x2]
roi_x=x2-x1
roi_y=y2-y1
# ball = img[170:305, 215:355]

# img[15:22, 65:67] = ball
def addRoiInImage(img ,ball_roi, x1,y1,x2,y2,roi_x,roi_y):
    x = x2-x1
    y= y2-y1
    if(x == roi_x and y== roi_y):
        img[y1:y2, x1:x2] = ball_roi
        print("all measure is good")
    else:
        print("inerting area is not equal to roi image size")

def replaceRoiInImage(img ,ball_roi,replace_img, x1,y1,x2,y2,roi_x,roi_y):
    x = x2-x1
    y= y2-y1
    if(x == roi_x and y== roi_y):
        print("all measure is good")
        print(replace_img.shape ,ball_roi.shape)
        if(replace_img.shape == ball_roi.shape):
            img[y1:y2, x1:x2] = replace_img
            print("replaced")
        else:
            print("replace size is not equal")
    else:
        print("inerting area is not equal to roi image size")

cat_img = cv2.imread("cat.png")
ball_roi_x , ball_roi_y ,ball_roi_chnl= ball_roi.shape
print(ball_roi.shape)
cat_img = cv2.resize(cat_img,(ball_roi_y,ball_roi_x))
# addRoiInImage(img,ball_roi,14,22,62,67,roi_x,roi_y)
dst = cv2.addWeighted(cat_img,0.8,ball_roi,0.3,0)
replaceRoiInImage(img,ball_roi,dst,241,0,289,45,roi_x,roi_y)

# replaceRoiInImage(img,ball_roi,cat_img,241,0,289,45,roi_x,roi_y)
# img[22:67,14:62] = ball_roi
# img[0:45,241:289] = ball_roi

# img[241:67, 292:45] = ball

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 14  ,  22
# 56  ,  67
# 241  ,  1
# 292  ,  45


# size= 50,45
