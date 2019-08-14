import cv2
import time
v=cv2.VideoCapture(0)
time.sleep(2)
while(1):
    d,i=v.read()
    fd=cv2.CascadeClassifier(r'C:\Users\**\AppData\Local\Programs\Python\Python35\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')#there must be path of haarcascade_frontalface_alt.xml file
    face=fd.detectMultiScale(i,1.3,9)
    print(face)
    if(len(face)==1):
        print('face is available')
        x=face[0,0]
        y=face[0,1]
        w=face[0,2]
        h=face[0,3]
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('my image',i)
    k=cv2.waitKey(5)
    if(k==ord('q')):
        cv2.destroyAllWindows()
        break
