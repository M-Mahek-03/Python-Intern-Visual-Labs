import cv2
import numpy as np
import subprocess
import HandTrackingModule as htm
import math

################################
wCam, hCam = 640, 480
################################o

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

cap = cv2.VideoCapture(0)
detector = htm.HandsDetector(detection_con=0.7, max_hands=1)

def set_system_volume(volume):
    # Construct the AppleScript command
    applescript = f'tell application "System Events" to set volume output volume {int(volume)}'

    # Execute the AppleScript command using osascript
    subprocess.run(["osascript", "-e", applescript], capture_output=True)

while True:
    success, img = cap.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)
    if len(lm_list) != 0:
        x1, y1 = lm_list[4][1], lm_list[4][2]
        x2, y2 = lm_list[8][1], lm_list[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1) # Hand range 50 - 300
        # Volume Range 0 - 100

        vol = np.interp(length, [50, 300], [0, 100])
        print(int(length), vol)
        set_system_volume(vol)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Img", img)
    cv2.waitKey(1)

