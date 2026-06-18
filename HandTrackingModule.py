import cv2
import mediapipe as mp
import time
import math

class HandsDetector:
    def __init__(self, mode=False, max_hands=1, detection_con=0.7, track_con=0.6):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = int(detection_con * 100)  # Convert float to int percentage
        self.track_con = track_con
        
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands,
                                         self.detection_con, self.track_con)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_landmarks,
                                                self.mp_hands.HANDS_CONNECTIONS)
        return img

    def find_position(self, img, hand_no=0, draw=True):
        x_list = []
        y_list = []
        bbox = []
        lm_list = []
        results = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if results.multi_hand_landmarks:
            my_hand = results.multi_hand_landmarks[hand_no]
            for idx, lm in enumerate(my_hand.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                x_list.append(cx)
                y_list.append(cy)
                lm_list.append([idx, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            xmin, xmax = min(x_list), max(x_list)
            ymin, ymax = min(y_list), max(y_list)
            bbox = xmin, ymin, xmax, ymax
            if draw:
                cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                              (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)
        return lm_list, bbox

def main():
    p_time = 0
    
    detector = HandsDetector()
    while True:
        success, img = cv2.CAP_IMAGES.read()
        img = detector.find_hands(img)
        lm_list, _ = detector.find_position(img)
        if lm_list:
            print(lm_list[4])

        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
