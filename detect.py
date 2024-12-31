from ultralytics import YOLO
import cv2
import numpy as np
import time

# Load model YOLO
model = YOLO("best.pt")

# Buka kamera lokal (webcam)
cap = cv2.VideoCapture('video.mp4')  # 0 untuk kamera default, ubah ke 1 jika Anda memiliki beberapa kamera

# Cek apakah kamera berhasil dibuka
if not cap.isOpened():
    print("Tidak dapat membuka kamera")
    exit()

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame dari kamera")
        break

    # Melakukan prediksi menggunakan YOLO
    time_mulai = time.time()
    results = model.predict(frame, show=True, verbose=False)

    print("Waktu Prediksi:", time.time() - time_mulai)

    # Memproses hasil prediksi
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)
            cls_name = model.names[cls_id]
            if cls_name == "object":
                print("Terdeteksi object")
            else:
                print(f"Terdeteksi {cls_name}")

    # Menunggu selama 1 ms untuk menanggapi input
    key = cv2.waitKey(1)
    if key == ord('q'):  # Tekan 'q' untuk keluar
        break

# Membebaskan sumber daya
cap.release()
cv2.destroyAllWindows()
