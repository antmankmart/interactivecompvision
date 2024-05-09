import cv2
import mediapipe as mp

#create window for camera capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

#get the drawing solution from mediapipe library
mp_drawing = mp.solutions.drawing_utils

#get the hands solution from mediapipe library
mp_hands = mp.solutions.hands

#create an instance of the hands solution
hand = mp_hands.Hands()


#loop through the frames and process each frame using hands
while True:
    success, frame = cap.read()
    if success:
        #convert the bgr frame from cv2 to rgb for mediapipe
        RGB_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #store processed frame
        result = hand.process(frame)

        #print the hand landmarks
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                print(hand_landmarks)
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        #show the result of the processing
        cv2.imshow("capture image", frame)
        
        #stop displaying if user presses q
        if cv2.waitKey(1) == ord('q'):
            break
cv2.destroyAllWindows()