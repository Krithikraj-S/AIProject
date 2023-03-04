# AI Project
## VIT ID RECOGNIZER
Marking attendence for 70 people each hour is tough and takes about 5 minutes of a teacher's class hours. And with the increasing amount of proxies we bring an automatic attendence marker that recognizes the register number of a student from their ID and automatically marks attendance for that student.
All the faculty has to do is give the slot number and the date and an excel sheet list with all the student's name and this app continues to do the rest of the job :)

## PYTHON LIBRARIES USED:

(i)**OpenCV**:
> OpenCV is a library of programming functions mainly for real-time computer vision. Using this module we capture the live video frame from the camera thus enabling us to process each and every frame to get data.

(ii)**Tesseract OCR**:
> Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images. Using this we extract the text from a frame of the live video feed we capture and then we use regular expressions to extract just the registration number from the list of words captured.

(iii)**Openpxyl**:
> Openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files. Using this librabry we access the namelist excel sheet uploaded and mark present for the registration number recognized.
