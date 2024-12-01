import cv2 as cv
img =cv.imread(r"data/yesil_elma.jpg")
#satır*sutun
print("yükseklik , genişlik , kanal sayısı(rgb)",img.shape)
print("yükseklik ==>",img.shape[0])
print("genişlik ==>",img.shape[1])
print("yükkanal sayısı(rgb) ==>",img.shape[2])

#veri türü 
print("Veri türü==>",img.dtype)

#görseli göster
cv.imshow("resim",img)
cv.waitKey(0)
cv.destroyAllWindows()