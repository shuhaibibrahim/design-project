# Design Project
# Odd-Even Implementation System

## Introduction

### What is Odd Even System?
A traffic rationing scheme to reduce the number of vehicles on the road. Vehicles with registration numbers ending with an odd digit will be allowed on roads on odd dates and those with an even digit on even dates.

### What is this Project?
To design and implement a system using computer vision that monitors vehicles on the road and report the vehicles that violates the traffic rationing scheme.

### Design Flow Diagram
![alt text](https://github.com/shuhaibibrahim/design-project/blob/master/flowchart.png)

### Design Steps
* Record live footage of vehicles on the road with a high resolution camera from major parts of the city.
* The recording is fed into YOLO V4 custom licence plate detecting model.
* The detected license plate image is then fed into Tesseract OCR engine (pytesseract) for recognizing the licence plate numbers.
* The above output string is then checked whether it violates the Odd-Even Scheme.
* If yes, The license plate string along with the date and time is inserted into the 'Vehicle Table'.

#### Database design
The database mainly consists of 3 tables.
* User Table
* Vehicle Table
* Vehicle Owner Table (From external database)

![alt text](https://github.com/shuhaibibrahim/design-project/blob/master/Database.jpg)


### Usecase diagram
![alt text](https://github.com/shuhaibibrahim/design-project/blob/master/usecase.png)

### Website
![alt text](https://github.com/shuhaibibrahim/design-project/blob/master/websiteUiLogin.jpeg)
![alt text](https://github.com/shuhaibibrahim/design-project/blob/master/websiteUiHome.jpeg)

* Consist of a Login page where the officers are allowed to login.
* A successful login leads to a page where the 'Vehicle Table' will be displayed.
* Option for searching by date is also provided.
