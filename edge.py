import cv2
import numpy as np

img = cv2.imread('dybala.jpg')

canny = cv2.Canny(img,50,200)

laplacian = cv2.Laplacian(img,cv2.CV_8U)

sobelx= cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
sobely= cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)
sobel= abs(sobelx)+abs(sobely)


cv2.imshow('original',img)
cv2.imshow('Canny Edge',canny)
cv2.imshow('laplacian Edge',laplacian )
cv2.imshow('sobel',np.uint8(sobel))
