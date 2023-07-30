import os
import cv2

rootDirectory="Testing"
Letters=26
ImgPerLetters=100

if not os.path.exists(rootDirectory):
    os.makedirs(rootDirectory)

camera=cv2.VideoCapture(0)

for label in range(26):
    if not os.path.exists(os.path.join(rootDirectory,str(label))):
        os.makedirs(os.path.join(rootDirectory,str(label)))
    
    while True:
        success,img=camera.read()
        cv2.putText(img,f'Press Q to Collect images for {chr(65+label)}',(100,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(150,255,0),2,cv2.LINE_AA)
        cv2.imshow("Ready to collect ?",img)
        key=cv2.waitKey(25)
        if key==ord('q'):
            break
        if key==ord('w'):
            camera.release()
            cv2.destroyAllWindows()
            exit(0)
    cv2.destroyAllWindows()
    counter=0
    while counter<ImgPerLetters:
        success,img=camera.read()
        cv2.imshow(f'Collecting Images for {chr(65+label)}',img)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(rootDirectory,str(label),f'{counter}.jpg'),img)
        counter+=1
    cv2.destroyAllWindows()

camera.release()
