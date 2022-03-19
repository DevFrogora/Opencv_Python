import cv2
import numpy as np

img = cv2.imread("hand.jpg")


#gaussian pyramid
layer = img.copy()
gaussian_pyramid =[layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid.append(layer)


#laplacian Pyramid

first_layer =  cv2.pyrDown(img)
expended_image = cv2.pyrUp(first_layer)
h ,w= expended_image.shape[0] ,expended_image.shape[1]
img = cv2.resize(img, (w,h))

laplacian = cv2.subtract(img,expended_image)

print(img.shape , expended_image.shape)


layer = gaussian_pyramid[5]
laplacian_pyramid =[layer]
for i in range(5,0,-1):
    size = ( gaussian_pyramid[i-1].shape[1] , gaussian_pyramid[i-1].shape[0])
    gaussian_expended = cv2.pyrUp(gaussian_pyramid[i],dstsize= size)
    laplacian = cv2.subtract(gaussian_pyramid[i-1],gaussian_expended)
    laplacian_pyramid.append(laplacian)
    # cv2.imshow(str(i),laplacian)


reconstructed_image = laplacian_pyramid[0]
# cv2.imshow("0 " , reconstructed_image)

for i in range(1,6):
    size = (laplacian_pyramid[i ].shape[1], laplacian_pyramid[i ].shape[0])
    reconstructed_image = cv2.pyrUp(reconstructed_image, dstsize = size)
    reconstructed_image =cv2.add(reconstructed_image,laplacian_pyramid[i])
    cv2.imshow(str(i), reconstructed_image)

# cv2.imshow("6 " , gaussian_pyramid[5])
# cv2.imshow("gaussian 0"+str(i), gaussian_pyramid[0])
# cv2.imshow("gaussian 5"+str(i), gaussian_pyramid[5])
# cv2.imshow("original image  " , img)
cv2.waitKey(0)
cv2.destroyAllWindows()