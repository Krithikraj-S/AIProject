import cv2 as cv
import pytesseract as pyt
import re
import numpy as np
import pandas as pd
import openpyxl as oxl

def check_id(frame):                                                  #checks for ID
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    myconfig = r"--psm 1 --oem 3"
    text  = pyt.image_to_string(thresh, config = myconfig)
    print(text);
    regex = r'[0-9]{2}[a-zA-Z]{3}[0-9]{4}'
    match = re.findall(regex, text)
    return match

def mark_attendence(reg_no):
    print(reg_no)
    F = input("Confirm registration number [Y/N]: ")
    if F=='N':
        return -1
    else:
        df.at[reg_no, date] = 'P'



capture = cv.VideoCapture(0)
cntr=0
flag = False
pyt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
slot = input("Slot: ")
inp = input("Date: ")
date = f'"{inp}"'
file_path = r"Book1.xlsx"
wb = oxl.load_workbook(file_path)

try:
    df = pd.read_excel(file_path, sheet_name=slot)
except ValueError:
    print("Please create appropriate Slot's name list")
    exit(0)
df.set_index('RegNo', inplace=True)

while True:

    ref,frame = capture.read()
    cv.imshow('Video',frame)
    cntr+=1

    if(cntr%30 == 0):
        match=check_id(frame)
        if match:
            print(match)
            f1=mark_attendence(match[0])
            if(f1==-1):
                continue
            ch= input("Finish attendance? [Y/N]:")
            if(ch=='Y'):
                flag = True
            

    
    if ((cv.waitKey(20) & 0xFF==ord('q')) | flag):
        break

capture.release()
cv.destroyAllWindows()
with pd.ExcelWriter(file_path, mode='a', if_sheet_exists="replace", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name=slot)
