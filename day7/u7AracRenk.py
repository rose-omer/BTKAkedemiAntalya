import cv2 as cv

img_togg = cv.imread(r"data/kirmizi_togg.jpg")
img_ferrari = cv.imread(r"data/kirmizi_ferrari.jpg")

b, g, r = cv.split(img_ferrari)

img_mavi = cv.merge((r, g, b))
img_yesil = cv.merge((b, r, g))
img_sari = cv.merge((b, r, r))
img_mor = cv.merge((r, g, r))

cv.imshow("Togg", img_togg)
cv.imshow("Ferrari", img_ferrari)

cv.imshow("Mavi", img_mavi)
cv.imshow("Yeşil", img_yesil)
cv.imshow("Sarı", img_sari)
cv.imshow("Mor", img_mor)

cv.waitKey(0)
cv.destroyAllWindows()
