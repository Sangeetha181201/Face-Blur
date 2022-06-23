#importing libraries
import cv2,time 

#Capturing the video
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
video=cv2.VideoCapture(0)

while True: 
check,frame=video.read() 
gray=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY) 

face=face_cascade.detectMultiscale(gray,scaleFactor=1.1,minNeighbour=5) 
for x,y,w,h in face: 
  
# Draw rectangle around the faces which is our region of interest
img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1) 

# applying a median blur over this new rectangle area
img[y:y+h,x:x+w]=cv2.medianblur(img[y:y+h,x:x+w],35) 

#display output
cv2.imshow("gotch !!!",frame)
key=cv2.waitKey(1) 

if key==ord('q'): 
  
  break video.release() 
  
  cv2.destroyAllwindows()
