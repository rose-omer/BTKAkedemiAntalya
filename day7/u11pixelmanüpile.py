import cv2 as cv
import numpy as np

# Görüntüyü yükle
img = cv.imread("data/elma.jpg")

# Eğer görüntü yüklenemezse hata mesajı ver
if img is None:
    print("Görüntü yüklenemedi. Dosya yolu doğru mu?")
    exit()

# Görüntü boyutunu al
height, width = img.shape[:2]
print("Genişlik ve Yükseklik: ", width, height)

# Beyaz kare için boyutlar
kare_boyut = 50
baslangic_x = (width // 2) - 25
baslangic_y = (height // 2) - 25

# Beyaz kareyi yerleştir
for y in range(baslangic_y, baslangic_y + kare_boyut):
    for x in range(baslangic_x, baslangic_x + kare_boyut):
        img[y, x] = [255, 255, 255]  # Beyaz renk

# Modifiye edilmiş görüntüyü göster
cv.imshow("Elma Görüntüsü", img)

# 'q' tuşuna basılınca pencereyi kapat
cv.waitKey(0)
cv.destroyAllWindows()
