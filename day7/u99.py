import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    # Kamera görüntüsünü okuyoruz
    ret, frame = cap.read()
    if not ret:
        break
    
    # Yatay aynalama (sol-sağ)
    mirror_frame_horizontal = cv.flip(frame, 1)
    
    # Görüntüleri iki farklı pencerede gösterme
    cv.imshow("Webcam - Yatay Aynalama", mirror_frame_horizontal) 
    cv.imshow("Orjinal", frame)
    
    # 'q' tuşuna basılınca döngüyü sonlandırıyoruz
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
