import cv2
import sounddevice as sd
import soundfile as sf


data, samplerate = sf.read("./beep.wav")

for idx, device in enumerate(sd.query_devices()):
    print(device)
    if 'USB PnP Sound Device' in device['name']:
        sd.default.device = idx
        break


myrecording = sd.playrec(data, samplerate, channels=1)
sd.wait()
sd.play(myrecording, samplerate)
sd.wait()

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

while cap.isOpened():
    # 카메라 프레임 읽기
    success, frame = cap.read()
    if success:
        # 프레임 출력
        cv2.imshow('Camera Window', frame)

        # ESC를 누르면 종료
        key = cv2.waitKey(1) & 0xFF
        if (key == 27):
            break

cap.release()
cv2.destroyAllWindows()