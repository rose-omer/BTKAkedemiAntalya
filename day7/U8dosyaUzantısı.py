import cv2 as cv
img =cv.imread("data/satranc3x3.jpg")

b,g,r=cv.split(img)
img_mavi=cv.merge((r,g,b))

cv.imwrite("data/satranc3x3.jpg_mavi.png",img_mavi)
cv.imwrite("data/satranc3x3.jpg_mavi.jpeg",img_mavi)
