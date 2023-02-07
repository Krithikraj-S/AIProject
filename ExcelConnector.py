import pandas as pd
import openpyxl as oxl

slot = input("Slot: ")
inp = input("Date: ")
date = f'"{inp}"'
file_path = "Book1.xlsx"
wb = oxl.load_workbook(file_path)

try:
    df = pd.read_excel(file_path, sheet_name=slot)
except ValueError:
    print("Please create appropriate Slot's name list")
    exit(0)


df.set_index('RegNo', inplace=True)

ch = 'N'
while ch=='N' or ch=='n':
    regno = input("Registration number: ")
    print(regno)
    F = input("Confirm registration number [Y/N]: ")
    if F=='N':
        continue

    df.at[regno, date] = 'P'

    ch = input("Finish attendance? [Y/N]:")

with pd.ExcelWriter(file_path, mode='a', if_sheet_exists="replace", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name=slot)