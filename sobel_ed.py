import numpy as np
import cv2

#a function for convolution operation
def Convolve(img,mask):
    row1total = img[0,1]*mask[0,1] + img[0,2]*mask[0,2] + img[0,0]*mask[0,0]
    row2total = 0
    row3total = img[2,1]*mask[2,1] + img[2,2]*mask[2,2] + img[2,0]*mask[2,0]
    return row1total + row2total + row3total

#a function for taking part of image to apply convolution between mask and part of image
def takePartImage(inpimg,i,j):
    image = np.zeros((3,3))
    a = i
    b = j
    for k in range(0,3):
        b = j
        for l in range(0,3):
            image[k,l] = inpimg[a,b]
            b = b+1
        a = a +1
    return image

#a function for finding X gradient
def SobelXgradient(inputimg):
    rows = len(inputimg)
    cols = len(inputimg[0])
    Gx = np.array(np.mat('1 0 -1; 2 0 -2; 1 0 -1'))
    outputimg = np.zeros((rows,cols))
    for i in range(0,rows-3):
         for j in range(0,cols-3):
             # retreve the part of image of 3 x 3 dimension from inputimage
             image  = takePartImage (inputimg, i, j)
             outputimg[i,j] = Convolve(image,Gx)
    return outputimg

#a function for finding Y gradient
def SobelYgradient(inputimg):
    rows = len(inputimg)
    cols = len(inputimg[0])
    #print(rows,cols)
    Gy = np.array(np.mat('-1 -2 -1; 0 0 0; 1 2 1'))
    outputimg = np.zeros((rows,cols))
    for i in range(0,rows-3):
         for j in range(0,cols-3):
             # retreve the part of image of 3 x 3 dimension from inputimage
             image  = takePartImage (inputimg, i, j)
             outputimg[i,j] = Convolve(image,Gy)
    return outputimg

#reading an image 
inputimg = cv2.imread('dybala1.jpg',0);

sobelimagex = SobelXgradient(inputimg)
sobelimagey = SobelYgradient(inputimg)

rows = len(inputimg)
cols = len(inputimg[0])

outputimg = np.zeros([rows, cols])

#finding the gradient magnitude by using the formula [abs(imgx) + abs(imgy)]
for i in range(0,rows):
    for j in range(0,cols):
        outputimg[i,j] = abs(sobelimagex[i, j]) + abs(sobelimagey[i, j])


sobel_x=abs(sobelimagex)
sobel_y=abs(sobelimagey)

cv2.imshow('original',inputimg)
cv2.imshow('sobel X',np.uint8(sobel_x))
cv2.imshow('sobel Y',np.uint8(sobel_y))
cv2.imshow('sobel image',np.uint8(outputimg))
cv2.waitKey(0)
