import cv2 as cv
# İşlemek istediğiniz resmin yolunu girin
input_image_path = "data/omer.png"  


image = cv.imread(input_image_path)
if image is None:
    print(f"Resim {input_image_path} yolunda bulunamadı.")
else:
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  
    rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)   
    hls_image = cv.cvtColor(image, cv.COLOR_BGR2HLS)   
    lab_image = cv.cvtColor(image, cv.COLOR_BGR2LAB)   
    hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)   
    inverted_image = cv.bitwise_not(image)             
    edge_image = cv.Canny(image, 100, 200)             
    mirrored_image = cv.flip(image, 1)                 

    def resize_image(img, scale=1.5):
        return cv.resize(img, (int(img.shape[1] * scale), int(img.shape[0] * scale)))

    image = resize_image(image)
    gray_image = resize_image(gray_image)
    rgb_image = resize_image(rgb_image)
    hls_image = resize_image(hls_image)
    lab_image = resize_image(lab_image)
    hsv_image = resize_image(hsv_image)
    inverted_image = resize_image(inverted_image)
    edge_image = resize_image(edge_image)
    mirrored_image = resize_image(mirrored_image)

    cv.imshow("Orjinal Resim", image)
    cv.imshow("Gri Tonlama", gray_image)
    cv.imshow("RGB Renk Uzayı", rgb_image)
    cv.imshow("HLS Renk Uzayı", hls_image)
    cv.imshow("LAB Renk Uzayı", lab_image)
    cv.imshow("HSV Renk Uzayı", hsv_image)
    cv.imshow("Ters Çevrilmiş (Negatif)", inverted_image)
    cv.imshow("Kenar Tespiti", edge_image)

    cv.imshow("Yatay Aynalama", mirrored_image)
    
    if cv.waitKey(0) == ord('s'):
        cv.imwrite("gray_image.png", gray_image)
        cv.imwrite("rgb_image.png", rgb_image)
        cv.imwrite("hls_image.png", hls_image)
        cv.imwrite("lab_image.png", lab_image)
        cv.imwrite("hsv_image.png", hsv_image)
        cv.imwrite("inverted_image.png", inverted_image)
        cv.imwrite("edge_image.png", edge_image)
  
        cv.imwrite("mirrored_image.png", mirrored_image)
        print("Tüm filtreler kaydedildi.")
    
    cv.destroyAllWindows()
