import cv2
import time
import random
nowTime= time.time()

def take_snapshot():
    capture= cv2.VideoCapture(0)
    result= True
    number= random.randint(0,100)
    while(result):
        accept,frame= capture.read()
        cv2.imwrite("Image"+str(number)+".png",frame)
        nowTime=time.time()
        result=False
    capture.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if(time.time()-nowTime>=5):
            take_snapshot()

main()