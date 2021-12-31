import cv2
import datetime

cap = cv2.VideoCapture(0);

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out= cv2.VideoWriter('output.mp4',fourcc,30,(640,480))

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(3,3000)
#cap.set(4,3000)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH) , cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(cap.isOpened()):
	ret , frame = cap.read()
	
	if ret == True:
	
		font = cv2.FONT_HERSHEY_SIMPLEX
		datet = str(datetime.datetime.now())
		text = 'Width: '+str(cap.get(3))+' Heigth: '+str(cap.get(4)) 
		

		frame = cv2.putText(frame,datet ,(10,70),font,1,(0,255,255),2,cv2.LINE_AA)
		out.write(frame)
		
		cv2.imshow('frame',frame )
		#gray = cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY)
		#cv2.imshow('frame',gray )
	
		if cv2.waitKey(1) == ord('q'):
			break
	else:
		break

out.release()
cap.release()
cv2.destroyAllWindows()