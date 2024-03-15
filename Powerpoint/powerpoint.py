import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(1)  # Adjust the camera index if necessary
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height=pyautogui.size()
index_y=0
index_x=0

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error reading frame from camera")
        continue

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        print("Detected hands:", len(hands))
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            # print("Number of landmarks:", len(landmarks))
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print("Landmark", id, ":", x, y)

                if id == 17: #pointer
                    cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    # pyautogui.moveTo(index_x,index_y)
                if id == 4:  #thumb
                    cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
                    middle_x=screen_width/frame_width*x
                    middle_y=screen_height/frame_height*y
                    # pyautogui.moveTo(middle_x, middle_y)
                    # print('outside', abs(index_y-middle_y))
                    if abs(index_x)<abs(middle_x):
                        print('right')
                        pyautogui.press('right')
                        pyautogui.sleep(2)
                    if abs(index_x) > abs(middle_x):
                        print('left')
                        pyautogui.press('left')
                        pyautogui.sleep(2)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
