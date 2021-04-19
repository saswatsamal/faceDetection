#main.py

#importing the OpenCV Lib
import cv2

#Loading the haarcascade front face file
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Reading the face image
img = cv2.imread('testFace.jpg')

#Converting the image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)

