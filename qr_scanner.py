import cv2
import webbrowser

camera = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, frame = camera.read()
    if not ret:
        continue

    data, _, _ = detector.detectAndDecode(frame)

    if data:
        print("QR Detected:", data)
        webbrowser.open(data)
        break

    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
