import numpy as np
import cv2
import datetime

def alper_geldi():
    print("Hoşgeldiiiinn!! Şu anda saat ve gün:")
    print(datetime.datetime.now())

def alper_gitti():
    print("Hoşçaakaal!! Bilgisayarı şu saatte bıraktın:")
    print(datetime.datetime.now())

cap = cv2.VideoCapture(0)
frameRate = cap.get(5)
ret, prev_frame = cap.read()
prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
pixels = prev_frame.shape[0] * prev_frame.shape[1]


alper_burada = True
counter = 0
alper_burada_skor = 0
while(cap.isOpened):
    # Capture frame-by-frame
    ret, frame = cap.read()
    counter += 1
    
    if(counter / frameRate > 3):
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst = cv2.absdiff(gray, prev_frame)

        # Display the resulting frame
        # cv2.imshow('frame',gray)
        # cv2.imshow('abs_diff',dst)
        prev_frame = gray
        diff = cv2.sumElems(dst)
        norm = diff[0] / (pixels)

        if((norm > 20) and (not alper_burada)):
            # Alper geldi!
            alper_burada = True
            alper_geldi()
        elif(norm < 2.3):
            alper_burada_skor -= 1
            if(alper_burada):
                print("Alper gitti, veya hareketsiz duruyor. Alperin burada olma puanı: {}".format(alper_burada_skor))
                if(alper_burada_skor < -5):
                    # Alper gitmiş olmalı!
                    alper_burada = False
                    alper_gitti()
        else:
            alper_burada_skor = 0
                


        counter = 0

    
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
