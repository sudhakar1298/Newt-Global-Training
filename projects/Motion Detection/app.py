import cv2 
import time 
import os
import glob 
from sendemails import send_mail


video=cv2.VideoCapture(0)
time.sleep(1)
sl=[]
c=0
first_frame=None

def clean_folder():
    images=glob.glob("images/*.png")
    for i in images:
        os.remove(i)


while True:
    s=0
    check,frame=video.read()
   
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray_frame_gau=cv2.GaussianBlur(gray_frame,(21,21),0)
    
    if first_frame is None:
        first_frame=gray_frame_gau
    
    delta_frane=cv2.absdiff(first_frame,gray_frame_gau)
    thresh_frame=cv2.threshold(delta_frane,45,255,cv2.THRESH_BINARY)[1]
    dil_frame=cv2.dilate(thresh_frame,None,iterations=2)
    counters,check=cv2.findContours(dil_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for co in counters:
        if cv2.contourArea(co)<5000:
            continue
        
        x,y,w,h=cv2.boundingRect(co)
        rect=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3 )
        print(type(rect))
        if rect.size!=0:
            s=1
            cv2.imwrite(f"images/{c}.png",frame)
            c+=1
            all_images=glob.glob("images/*.png")
            i=int(len(all_images)/2)
            imgnum=all_images[i]
    
    sl.append(s)
    sl=sl[-2:]
    if sl[0]==1 and sl[1]==0:
        send_mail(imgnum)
        clean_folder()

    cv2.imshow("My Video",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
video.release()