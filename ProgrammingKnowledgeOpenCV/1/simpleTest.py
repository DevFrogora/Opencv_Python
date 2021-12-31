import cv2
image_folder_path = 'C:\\Users\\5454\\Desktop\\pythonProject\\1\\'

img = cv2.imread(  'human.png',-1)

print(cv2.__version__)
print(img)

cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('human_copy.png',img)
	cv2.destroyAllWindows()