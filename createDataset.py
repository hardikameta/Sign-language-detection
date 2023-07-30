import pickle
import os
import mediapipe as mp
import cv2

rootDirectory='Testing'
mp_hands=mp.solutions.hands
hands=mp_hands.Hands(min_detection_confidence=0.3,static_image_mode=True)
# print("yes")
data=[]
labels=[]
for label in os.listdir(rootDirectory):
    for img_path in os.listdir(os.path.join(rootDirectory,str(label))):
        img=cv2.imread(os.path.join(rootDirectory,str(label),img_path))
        # print("yes")
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # print("yes")
        result=hands.process(img_rgb)
        # print("yes")
        if result.multi_hand_landmarks:
            landmarks=[]
            x_=[]
            y_=[]
            for hand_landmarks in result.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x=hand_landmarks.landmark[i].x
                    y=hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)
                for i in range(len(hand_landmarks.landmark)):
                    x=hand_landmarks.landmark[i].x
                    y=hand_landmarks.landmark[i].y
                    landmarks.append(x-min(x_))
                    landmarks.append(y-min(y_))
            data.append(landmarks)
            labels.append(label)

f=open('dataset.pickle','wb')
pickle.dump({'data':data,'labels':labels},f)
f.close()