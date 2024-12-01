import cv2
import numpy as np
import gradio as gr
# open cv de renk kanalları BGR  şekilde sıralanmıştır
# Mavi renk dışındaki her şeyi griye çeviren filtre


def kırmızı(frame):
    return apply_isolation(frame,(100,150,50),(150,255,255))

def mavi (frame):
    return apply_isolation(frame, (0, 150, 50), (50, 255, 255))

def yeşil (frame):
    return apply_isolation(frame, (35, 60, 20), (85, 255, 150))


def apply_isolation(frame, lower_color = (100, 150, 50) , upper_color = (150, 255, 255)):
  # Görüntüyü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Belirli renk aralığında kalan pikseller için bir maske oluştur
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # özel alanları koru, geri kalanları griye çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_colored = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)

    #  maskeyi kullanarak çıktı oluştur
    output = np.where(mask[:, :, None] == 0, gray_frame_colored, frame)

    return output


def apply_filter(filter_type,input_image=None):
    if filter_type is not None :
        frame=input_image
    else:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if not ret:
            return "Web kameradan görüntü alınamadı"


    if filter_type =="mavi filtre":
        return mavi(frame)
    elif filter_type =="kırmızı filtre":
        return  kırmızı(frame)
    elif filter_type =="yeşil filtre":
        return yeşil(frame)









# Gradio arayüzü tanımlanıyor
with gr.Blocks() as demo:
    gr.Markdown("# Mavi Renk Dışında Her Şeyi Griye Çevirme")

    # Filtre seçenekleri
    filter_type = gr.Dropdown(
        label="Filtre Seçin",
        choices=["mavi filtre","kırmızı filtre","yeşil filtre"],
        value="mavi filtre"
    )



    # Kullanıcıdan resim yüklemesi beklenen alan
    input_image = gr.Image(label="Resim Yükle", type="numpy")

    # Uygulanan filtre sonucu gösterilen çıktı görüntüsü
    output_image = gr.Image(label="Filtre Uygulandı")

    # Görüntü yüklendiğinde filtre fonksiyonunu çağırır
    input_image.change(fn=apply_filter, inputs=[filter_type,input_image], outputs=output_image)

# Gradio arayüzünü başlatır
demo.launch()
