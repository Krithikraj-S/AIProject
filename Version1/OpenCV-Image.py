import cv2 as cv
import pytesseract as pyt
import re
import numpy as np

capture = cv.VideoCapture(0)
cntr=0
flag = False

while True:

    ref,frame = capture.read()
    cv.imshow('Video',frame)
    cntr+=1

    if(cntr%30 == 0):
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
        myconfig = r"--psm 1 --oem 3"
        text  = pyt.image_to_string(thresh, config = myconfig)
        regex = r'[0-9]{2}[a-zA-Z]{3}[0-9]{4}'
        match = re.findall(regex, text)
        if match:
            print(match[0])
            flag = True

    if ((cv.waitKey(20) & 0xFF==ord('q')) | flag):
        break

capture.release()
cv.destroyAllWindows()



