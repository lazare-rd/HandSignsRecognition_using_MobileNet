import cv2
import time
import os
import uuid
import Setup

nbOfPhotos = 5
LABELS = ["thankYou", "peace", "thumbUp", "thumbDown"]

def takeAPhoto():
    cap = cv2.VideoCapture(0)
    print("La photo sera prise dans 5s")
    time.sleep(5)
    ret, frame = cap.read()
    imgname = os.path.join(Setup.paths['IMAGE_PATH'], "train_bis",  "thumbUp" +'.'+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame', frame)
    cap.release()
    cv2.destroyAllWindows()

def buildPhotoDeck():
    for label in LABELS:
        cap = cv2.VideoCapture(0)
        print("Les photos commenceront dans 5s")
        time.sleep(5)
        for i in range(nbOfPhotos):
            print("Collecting photo" + label + " #" + str(i))
            ret, frame = cap.read()
            imgname = os.path.join(Setup.paths['IMAGE_PATH'], "train_bis",  label +'.'+'{}.jpg'.format(str(uuid.uuid1())))
            time.sleep(2)
            cv2.imwrite(imgname, frame)
            cv2.imshow('frame', frame)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__' : 
    takeAPhoto()
    #buildPhotoDeck()