import cv2
import numpy as np

img1 = cv2.imread("baseball_ball.png")
img1 = cv2.resize(img1,(1000,1000))
img2 = cv2.imread("football_ball.png")
img2 = cv2.resize(img2,(1000,1000))


footbase_ball = np.hstack((img1[:,:500] , img2[:,500:]))


#gaussian pyramid 1
layer = img1.copy()
gaussian_pyramid =[layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)

#laplician pyramid 1
layer = gaussian_pyramid[5]
laplacian_pyramid =[layer]
for i in range(5,0,-1):
    size = ( gaussian_pyramid[i-1].shape[1] , gaussian_pyramid[i-1].shape[0])
    gaussian_expended = cv2.pyrUp(gaussian_pyramid[i],dstsize= size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1],gaussian_expended)
    laplacian_pyramid.append(laplacian)



#gaussian pyramid 2
layer = img2.copy()
gaussian_pyramid2 =[layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid2.append(layer)

#laplician pyramid 2
layer = gaussian_pyramid2[5]
laplacian_pyramid2 =[layer]
for i in range(5,0,-1):
    size = ( gaussian_pyramid2[i-1].shape[1] , gaussian_pyramid2[i-1].shape[0])
    gaussian_expended = cv2.pyrUp(gaussian_pyramid2[i],dstsize= size)
    laplacian = cv2.subtract(gaussian_pyramid2[i-1],gaussian_expended)
    laplacian_pyramid2.append(laplacian)



#laplician pyramid footbase_ball
footbase_ball_pyramid =[]
n=0
for img1_lap ,img2_lap in zip(laplacian_pyramid,laplacian_pyramid2):
    n +=1
    cols, rows , ch =img1_lap.shape
    laplacian = np.hstack((img1_lap[:, :int(cols/2)], img2_lap[:, int(cols/2):]))
    cv2.imshow(str(n),laplacian)
    footbase_ball_pyramid.append(laplacian)
    cv2.imshow(str(i), laplacian)



footbase_ball_reconstructed = footbase_ball_pyramid[0]
# cv2.imshow("0 " , reconstructed_image)

for i in range(1,6):
    size = (footbase_ball_pyramid[i ].shape[1], footbase_ball_pyramid[i ].shape[0])
    footbase_ball_reconstructed = cv2.pyrUp(footbase_ball_reconstructed, dstsize = size)
    footbase_ball_reconstructed =cv2.add(footbase_ball_reconstructed,footbase_ball_pyramid[i])
    # cv2.imshow(str(i), footbase_ball_reconstructed)

cv2.imshow("footbase_ball_reconstructed" , footbase_ball_reconstructed)
cv2.waitKey(0)
cv2.destroyAllWindows()