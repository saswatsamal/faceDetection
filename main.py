#importing the OpenCV Lib
import cv2

#Loading the haarcascade front face file
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the face image
img = cv2.imread('testFace.jpg')

#Converting the image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting the face
face = faceCascade.detectMultiScale(gray, 1.1,4)

#Draw rectangle around the face
for(x,y,w,h) in face:
    cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),2)

#Display the result with face detected
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
