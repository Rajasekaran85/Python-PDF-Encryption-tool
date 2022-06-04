import os
import re
from pikepdf import Pdf

print("\n PDF Encryption Tool \n")
print("\n Developed by A Rajasekaran\n")
print("\n Date: 03 June 2022 \n\n")

'''
- Password value should capture in the "password.ini" file, within the <Password> tags
- INI file should place in the tool location
- 128-bit encryption Output PDF can be open Acrobat (or) Reader 7 or later
- 256-bit encryption Output PDF can be open Acrobat (or) Reader 9 or later
- Encryption value should be any one value : "128" or "256"
'''

filepath1 = input(" Enter the File path: ")

filepath = filepath1 + "\\"

filelist = os.path.isdir(filepath)

directory = "Output"

Out = filepath + directory

meta = "password.ini"  # password should update in the INI file.

if os.path.exists(meta): # check the password.ini file present
    pass
else:
    print("\n password.ini file is missing")

if os.path.exists(Out):  # create the Output folder
    pass
else:
    os.mkdir(Out)

fo = open(meta, "r+", encoding="utf-8")   # password ini file will open and stored the values in "str1" variable
str1 = fo.readlines()

pas = re.search(r"<Password>(.*)</Password>", str(str1))  # get the value from the INI file using regex pattern and store in the variable
password = pas.group(1)

lev = re.search(r"<Level>(.*)</Level>", str(str1))
level = lev.group(1)

value1 = "128"
value2 = "256"

fo.close()

for fname in os.listdir(filepath):
	if not fname.endswith(".pdf"):
		continue
	with Pdf.open(filepath + fname) as pdf:     # each pdf file will open and file store in the variable "pdf"
		outputfile = Out + "\\" + fname
		if (password == ""): # if password value not entered then notify this message
			print("\n\n Password value not entered in the INI file")
			break
		else:
			pass
		if (value1 != level) and (value2 != level): #checking the encryption value 128 or 256
			print("\n\n Encryption level is value not correct, value should be any one: 128 or 256")
			break
		else:
			pass
		if (value1 == level):
			pdf.save(outputfile, linearize=True, encryption=dict(owner=password, R=4))  # R = 4 defines 128-aes encryption, 5 defines 256-aes encryption
			print(fname + " - 128-bit AES Encryption")
		if (value2 == level):
			pdf.save(outputfile, linearize=True, encryption=dict(owner=password, R=5)) 
			print(fname + " - 256-bit AES Encryption")
		pdf.close()



