import cv2 as cv
# Görüntü yükleme
img_bgr = cv.imread("data/elma.jpg")
# Renk kanallarının ayrılması
b,g,r=cv.split(img_bgr)

# renk efekt oluşturma

img_mavi=cv.merge((r,g,b))
img_yesil=cv.merge((b,r,g))
img_sari=cv.merge((b,r,r))
img_mor=cv.merge((r,g,r))
# Efekt görüntülerini gösterme
cv.imshow("orjinal",img_bgr)
cv.imshow("mavi",img_mavi)
cv.imshow("yesil",img_yesil)
cv.imshow("sari",img_sari)
cv.imshow("sari",img_mor)

cv.waitKey(0)
cv.destroyAllWindows()