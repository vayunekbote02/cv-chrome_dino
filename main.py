import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8, maxHands=1)

video = cv2.VideoCapture(0)

thumb_key_pressed = False
index_key_pressed = False

while True:
    ret, frame = video.read()
    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)
    
    if hands:
        lmList = hands[0]
        fingers_up = detector.fingersUp(lmList)
        
        if fingers_up == [1, 0, 0, 0, 0]:  # Thumb position
            cv2.putText(frame, "Thumb", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Duck", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            if not thumb_key_pressed:
                pyautogui.keyDown('down')
                thumb_key_pressed = True
                index_key_pressed = False
        elif fingers_up == [0, 1, 0, 0, 0]:  # Index finger position
            cv2.putText(frame, "Index", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Jump", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            if not index_key_pressed:
                pyautogui.keyDown('space')
                index_key_pressed = True
                thumb_key_pressed = False
        else:  # No specific finger position detected
            cv2.putText(frame, "Closed", (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, "Running", (420, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
            if thumb_key_pressed:
                pyautogui.keyUp('down')
                thumb_key_pressed = False
            if index_key_pressed:
                pyautogui.keyUp('space')
                index_key_pressed = False

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

