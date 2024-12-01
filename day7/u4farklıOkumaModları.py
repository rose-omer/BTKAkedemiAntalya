import cv2 as cv

# gri sıkala
img_bgr =cv.imread("data/satranc3x3.jpg")
img_gri =cv.imread("data/satranc3x3.jpg",0)

#görseli göster
cv.imshow("Normal sıkala",img_bgr)
cv.imshow("Gri sıkala",img_gri)
cv.waitKey(0)
cv.destroyAllWindows()