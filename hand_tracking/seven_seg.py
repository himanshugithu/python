import cv2
import time
import handtrackingmodule as htm
import serial

arduinoData = serial.Serial("com3",9600)
ptime = 0

cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.75)
tipIds = [4,8,12,16,20]
while True:
    sucess,img = cap.read()
    img = detector.findHands(img)
    lmlist= detector.findPosition(img,draw=False)
    # print(lmlist)
    if len(lmlist) != 0:
        fingers = []

  #thumb
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
                fingers.append(1)
        else:
            fingers.append(0) 

        # if lmlist[tipIds[0]][1] < lmlist[tipIds[0]-2][1]:
        #         fingers.append(1)
        # else:
        #     fingers.append(0)     

        #4 finger
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0) 
        # print(fingers)          
        totalfinger = fingers.count(1)
        print(totalfinger)
        cv2.rectangle(img,(500,350),(650,485),(0,255,0),-1)
        cv2.putText(img,f"{int(totalfinger)}",(540,450),
                cv2.FONT_HERSHEY_PLAIN,6,(0,0,255),6)
        ranstr =  str(totalfinger)+'\r'
        arduinoData.write(ranstr.encode())          

    img = cv2.resize(img,[440,400])
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime= ctime
    cv2.putText(img,f"FPS : {int(fps)}",(40,70),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
        

    cv2.imshow("video",img)
    cv2.waitKey(1)