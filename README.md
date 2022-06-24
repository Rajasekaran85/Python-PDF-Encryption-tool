# Project Title

PDF Encryption Application

## Description

PDF Encryption tool: Applying the Security settings (Restrictions).
Security Method: Password Security
Documents not allowed: Printing, Commenting, Changing the Documents, Signature, Document Assembly, Content Copying, Page Extraction
Password values should provide in the "meta.ini" file, tool will read this ini file and apply the security in the PDF file.

## Getting Started

### Dependencies

* Windows 7

### Installing

* pip install pikepdf

### Executing program

* password.ini file should copied in the tool path
* Run the program
* Tool will ask to enter the path of the input pdf file
* Tool execute the pdf files and create the output split pdf in the "Output" folder of the same input file  path

### Help

* Enter the password values in the password.ini file, example: ```<Password>Test123@</Password>```
* Also enter the encryption level in the password.ini file, values should be "128" or "256" any one required, example: ```<Level>128</Level>``` (or) ```<Level>256</Level>```
* Above both fields values are mandatory


## Version History

* 0.1
    * Initial Release
