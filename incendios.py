import numpy as np
import cv2 as cv
import math

cap = cv.VideoCapture('D:/tec/9no Semestre/IA/actividad/incendio/incendio3.mp4')
i=0
while True:
    ret, frame = cap.read()
    cv.imshow('img', frame)
    k = cv.waitKey(1)
    #if k==orf('a'):
    i=i+1
    cv.imwrite('D:/tec/9no Semestre/IA/actividad/dataset'+str(i)+'.jpg',frame)
    if k == 27:
        break
        cap.release()
        cv.destroyAllWindows()
