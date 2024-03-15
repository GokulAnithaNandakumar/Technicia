# import cv2
# import mediapipe as mp
# import pyautogui
#
# cap = cv2.VideoCapture(1)  # Adjust the camera index if necessary
# hand_detector = mp.solutions.hands.Hands()
# drawing_utils = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()
#
# # Variables to keep track of previous finger positions
# prev_index_x, prev_middle_x, prev_ring_x = None, None, None
#
# while True:
#     ret, frame = cap.read()
#     if not ret or frame is None:
#         print("Error reading frame from camera")
#         continue
#
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks
#     if hands:
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks = hand.landmark
#             index_x, middle_x, ring_x = None, None, None
#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)
#
#                 if id == 8:  # Index
#                     cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
#                     index_x = screen_width / frame_width * x
#
#                 if id == 12:  # Middle
#                     cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
#                     middle_x = screen_width / frame_width * x
#
#                 if id == 16:  # Ring
#                     cv2.circle(frame, center=(x, y), radius=15, color=(0, 255, 255))
#                     ring_x = screen_width / frame_width * x
#
#             # Check if finger positions are detected
#             if index_x is not None and middle_x is not None and ring_x is not None:
#                 # Move mouse along with fingers (optional)
#                 # pyautogui.moveTo(index_x, screen_height / 2)
#
#                 # Determine direction of swipe based on previous finger positions
#                 if prev_index_x is not None and prev_middle_x is not None and prev_ring_x is not None:
#                     # Calculate the change in finger x-coordinates
#                     index_dx = index_x - prev_index_x
#                     middle_dx = middle_x - prev_middle_x
#                     ring_dx = ring_x - prev_ring_x
#
#                     # Define threshold for detecting swipe movement
#                     SWIPE_THRESHOLD = 50
#
#                     # Check if all fingers moved in the same direction
#                     if abs(index_dx) > SWIPE_THRESHOLD and abs(middle_dx) > SWIPE_THRESHOLD and abs(ring_dx) > SWIPE_THRESHOLD:
#                         # Check direction of swipe (left or right)
#                         if index_dx > 0 and middle_dx > 0 and ring_dx > 0:
#                             pyautogui.hotkey('ctrl', 'right')  # Swipe right (Ctrl + Right Arrow)
#                             pyautogui.sleep(1)
#                         elif index_dx < 0 and middle_dx < 0 and ring_dx < 0:
#                             pyautogui.hotkey('ctrl', 'left')  # Swipe left (Ctrl + Left Arrow)
#                             pyautogui.sleep(1)
#
#                 # Update previous finger positions
#                 prev_index_x, prev_middle_x, prev_ring_x = index_x, middle_x, ring_x
#
#     cv2.imshow('Gesture Detection', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui
#
# cap = cv2.VideoCapture(1)  # Adjust the camera index if necessary
# hand_detector = mp.solutions.hands.Hands()
# drawing_utils = mp.solutions.drawing_utils
# screen_width, screen_height=pyautogui.size()
# index_y=0
#
# while True:
#     ret, frame = cap.read()
#     if not ret or frame is None:
#         print("Error reading frame from camera")
#         continue
#
#     frame = cv2.flip(frame, 1)
#     frame_height, frame_width, _ = frame.shape
#
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = hand_detector.process(rgb_frame)
#     hands = output.multi_hand_landmarks
#     if hands:
#         # print("Detected hands:", len(hands))
#         for hand in hands:
#             drawing_utils.draw_landmarks(frame, hand)
#             landmarks = hand.landmark
#             # print("Number of landmarks:", len(landmarks))
#             for id, landmark in enumerate(landmarks):
#                 x = int(landmark.x * frame_width)
#                 y = int(landmark.y * frame_height)
#                 print("Landmark", id, ":", x, y)
#
#                 if x>2000:
#                     pyautogui.hotkey('ctrl', 'right')  # Swipe right (Ctrl + Right Arrow)
#                     pyautogui.sleep(1)
#                 if x < 0:
#                     pyautogui.hotkey('ctrl', 'left')  # Swipe right (Ctrl + Right Arrow)
#                     pyautogui.sleep(1)
#
#     cv2.imshow('Virtual Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()


import cv2
import mediapipe as mp
import pyautogui
import time

cap = cv2.VideoCapture(1)  # Adjust the camera index if necessary
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

last_landmark_time = time.time()  # Initialize time for last landmark reading

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error reading frame from camera")
        continue

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Check if it's time to read the landmark again
    if time.time() - last_landmark_time >= 1:  # Check if 1 seconds have passed
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        last_landmark_time = time.time()  # Update last landmark reading time

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                x = int(landmarks[0].x * frame_width)
                y = int(landmarks[0].y * frame_height)
                print("Hand position:", x, y)

                # Map hand movements
                if x > 1500:
                    pyautogui.hotkey('ctrl', 'right')  # Swipe right (Ctrl + Right Arrow)
                if x < 370:
                    pyautogui.hotkey('ctrl', 'left')  # Swipe left (Ctrl + Left Arrow)

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
