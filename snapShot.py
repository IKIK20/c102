import cv2

def take_snapshot():
    #initializing cv2
    capture = cv2.VideoCapture(0)
    result = True
    while(result):
        #Read the frames while the camera is on
        ret, frame = capture.read()
        #To save the image on the local storage
        cv2.imwrite("Picture1.jpg", frame)
        result = False
    #Releases the camera
    capture.release()
    #Closes all windows that were opened by cv2
    cv2.destroyAllWindows()

take_snapshot()