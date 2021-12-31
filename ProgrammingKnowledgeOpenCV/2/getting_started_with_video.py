import cv2

cap = cv2.VideoCapture(0);

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out= cv2.VideoWriter('output.mp4',fourcc,30,(640,480))

while(cap.isOpened()):
	ret , frame = cap.read()
	
	if ret == True:
	
		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	
		out.write(frame)
		
		gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray )
	
		if cv2.waitKey(1) == ord('q'):
			break
	else:
		break

out.release()
cap.release()
cv2.destroyAllWindows()