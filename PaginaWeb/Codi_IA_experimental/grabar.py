import cv2
import os
import time 
import uuid
import sys 
import anvil.server

 


IMAGES_PATH  =  "Tensorflow\workspace\images\collectedimagess"

# Nombre de las letras a traducir

labels = ["u", "i", "o"]
number_imgs = 15

daleAelVideo = True
os.chdir("/Users/andre/RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages")



for x in labels:
    try:
        os.makedirs(x)

    except:
        pass
for label in labels:

    cap = cv2.VideoCapture(0)
    pathTrue = "/Users/andre/RealTimeObjectDetection/Tensorflow/workspace/images/collectedimages"

    os.chdir(pathTrue+"/"+label)


    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        cap = cv2.VideoCapture(0) 
        time.sleep(5)
        ret, frame = cap.read()

        imagename = label+"."+"{}.jpg".format(str(uuid.uuid1()))

        cv2.imwrite(imagename, frame)
        cv2.imshow("frame",frame)
        time.sleep(3)

        if cv2.waitKey(1) and 0xFF == ord("q"):

            break 

    cap.release()

cv2.destroyAllWindows()


