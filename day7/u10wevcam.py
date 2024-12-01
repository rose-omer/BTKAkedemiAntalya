import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    # Kamera görüntüsünü okuyoruz
    ret, frame = cap.read()
    if not ret:
        break

    # Renk dönüşümleri yapıyoruz
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)   
    hls_frame = cv.cvtColor(frame, cv.COLOR_BGR2HLS)    
    lab_frame = cv.cvtColor(frame, cv.COLOR_BGR2LAB)   
    hvs_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    flip_frame=cv.flip(frame,-1)
    # Üç farklı pencereyi açıyoruz
    cv.imshow("Webcam", frame)          
    cv.imshow("Webcam GRAY", gray_frame) 
    cv.imshow("Webcam RGB", rgb_frame)  
    cv.imshow("Webcam HLS", hls_frame)  
    cv.imshow("Webcam LAB", lab_frame)  
    cv.imshow("Webcam HVS", hvs_frame) 
    cv.imshow("Webcam FLİP", flip_frame) 

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
