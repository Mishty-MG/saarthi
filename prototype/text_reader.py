
import cv2
import pytesseract
import pyttsx3

# Connect Python to Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Set up speech
speaker = pyttsx3.init()
speaker.setProperty("rate", 155)


def read_text(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Could not open the image. Check its file path.")
        return

    text = pytesseract.image_to_string(image).strip()

    if text:
        print("\nRecognized text:")
        print(text)

        print("\nSaarthi is speaking...")
        speaker.say(text)
        speaker.runAndWait()
    else:
        print("No text found. Try a clearer image.")


if __name__ == "__main__":
    print("Saarthi Text Reader")
    image_path = input("Enter the image file path: ").strip().strip('"')
    read_text(image_path)
