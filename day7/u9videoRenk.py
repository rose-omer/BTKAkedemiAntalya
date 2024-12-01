import cv2 as cv
import numpy as np
#kameradan video
#cap=cv.VideoCapture(0)

#datadan video alma
input_video=r'data/araba_video.mp4'
cap=cv.VideoCapture(input_video)
    

#video özellikleri
fourcc=cv.VideoWriter_fourcc(*"mp4v")#kodek
fps =int(cap.get(cv.CAP_PROP_FPS))#FPS
witdh =int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height =int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

out=cv.VideoWriter("data/video.mp4",fourcc,fps,(witdh,height))
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    
    b,g,r=cv.split(frame)
    rgb_frame=cv.merge((r,g,b))
    cv.imshow("Mavi araba ==>" ,rgb_frame) #görseli göster
    out.write(rgb_frame)
    
    if cv.waitKey(1)==ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()