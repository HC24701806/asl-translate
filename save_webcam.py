import cv2
import time
import generateText

def recVideo(): 
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
    else:
        while True:
            # Capture a frame from the webcam
            ret, frame = cap.read()
            if ret:
                cv2.imwrite('./ImageInputs/photo.jpg', frame)
                time.sleep(1)
            else:
                print("Error: Could not capture an image.")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()