import cv2 as cv

# Resmi okuma
img = cv.imread(r'data/monalisa.jpg')

# Orijinal resmi gösterme
cv.imshow('Orijinal', img)
print(img.shape[:2])

# Resme çizgi ekleme
cv.line(img, (0, 0), (534, 720), (0, 0, 255), thickness=3)
cv.line(img, (534, 0), (0, 720), (0, 0, 255), thickness=3)

# Metin ekleme (Fontu ve diğer parametreleri düzelttik)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'Fake Mona Lisa', (150, 360), font, 1, (255, 0, 0), 2, cv.LINE_AA)

# Çizgi ve metin eklenmiş resmi gösterme
cv.imshow('Cizgi Metin', img)

# Bekleme ve pencereyi kapatma
cv.waitKey(0)
cv.destroyAllWindows()
