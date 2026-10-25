
import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open camera.")
    raise SystemExit

print("Saarthi Arrow Shape Test")
print("Show ONE large, dark arrow on a white background.")
print("Press SPACE to scan; Q to quit.")

while True:
    success, frame = camera.read()

    if not success:
        print("Could not capture a camera frame.")
        break

    cv2.imshow("Saarthi - Arrow Shape Test", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord(" "):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        _, binary = cv2.threshold(
            blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        contours, _ = cv2.findContours(
            binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        candidates = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= 500:
                perimeter = cv2.arcLength(contour, True)
                polygon = cv2.approxPolyDP(
                    contour, 0.025 * perimeter, True
                )
                x, y, w, h = cv2.boundingRect(contour)
                candidates.append((area, polygon, x, y, w, h))

        if not candidates:
            print("No clear shape found. Try a larger arrow.")
            continue

        # Inspect the largest dark shape in the image.
        area, polygon, x, y, w, h = max(candidates, key=lambda item: item[0])
        points = polygon.reshape(-1, 2)
        cx = x + w / 2
        cy = y + h / 2

        print(
            f"Shape found: area={area:.0f}, "
            f"vertices={len(points)}, width={w}, height={h}"
        )

        if len(points) < 5:
            print("Shape is too simple to identify confidently.")
        else:
            # Estimate direction from the farthest point from the shape centre.
            distances = ((points[:, 0] - cx) ** 2 +
                         (points[:, 1] - cy) ** 2)
            tip = points[distances.argmax()]
            dx = tip[0] - cx
            dy = tip[1] - cy

            if abs(dx) > abs(dy) * 1.2:
                direction = "RIGHT" if dx > 0 else "LEFT"
                print("Estimated direction:", direction)
            elif abs(dy) > abs(dx) * 1.2:
                direction = "DOWN" if dy > 0 else "UP"
                print("Estimated direction:", direction)
            else:
                print("Direction unclear. Try a cleaner arrow.")

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
