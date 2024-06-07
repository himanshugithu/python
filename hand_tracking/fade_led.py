import math
import cv2
import time
import handtrackingmodule as htm
import numpy as np
import serial
arduinoData = serial.Serial("com3",9600)




ptime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.7)




while True:
    sucess ,img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img,draw = False)
    if len(lmList) != 0:
        #print(lmList[2],lmList[4])
        x1,y1= lmList[4][1],lmList[4][2]
        x2,y2= lmList[8][1],lmList[8][2]

        # cx,cy = (x1 + x2) // 2, ( y2+y2 ) // 2

        cv2.circle(img,(x1,y1),8,(0,255,255),-1)
        cv2.circle(img,(x2,y2),8,(0,255,255),-1)
        cv2.line(img,(x1,y1),(x2,y2),(255,0,255),5)
        # cv2.circle(img,(cx,cy),8,(255,0,255),-1)
        lenth = math.hypot(x2 - x1, y2 - y1)
        lenth = int(lenth)
        # print(lenth)
        ran = np.interp(lenth,[20,130],[0,255])
        cv2.circle(img,(100,100),(int(ran//3)),(0,0,ran),-1)
        ranstr =  str(ran)+"\r"
        arduinoData.write(ranstr.encode())

                
        

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime=ctime
    cv2.putText(img,f"FPS : {int(fps)}",(40,70),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    cv2.imshow("img",img)
    cv2.waitKey(1)
