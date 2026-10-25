
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera.")
    raise SystemExit

print("Saarthi Live Reader")
print("Press Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not capture a camera frame.")
        break

    cv2.imshow("Saarthi - Live Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press SPACE to read text from the current frame
    if key == ord(" "):
        text = pytesseract.image_to_string(frame).strip()

        if text:
            print("\nRecognized text:")
            print(text)
        else:
            print("\nNo text found. Try holding the text closer.")

    # Press Q to close the camera
    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
