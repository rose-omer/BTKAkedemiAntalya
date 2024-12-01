import cv2 as cv
img =cv.imread("data/satranc3x3.jpg")

print(img)
cv.imshow("resim",img)
cv.waitKey(0)
cv.destroyAllWindows()