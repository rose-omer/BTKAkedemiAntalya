import cv2

# Resmi yükle
img = cv2.imread('data/gol_manzarasi.jpeg')

# Resmin boyutlarını al
h, w = img.shape[:2]

# Kırpılacak alanın başlangıç ve bitiş koordinatlarını hesapla
start_row, start_col = int(h * .25), int(w * .25)
end_row, end_col = int(h * .75), int(w * .75)

# Resmi kırp
cropped_img = img[start_row:end_row, start_col:end_col]

# Kırpılmış görüntü boyutunu yazdır
print(f"Kırpılmış Görüntü Boyutu: {cropped_img.shape}")

# Kırpılmış resmi göster
cv2.imshow('Crop', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
