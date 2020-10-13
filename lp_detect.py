import cv2
import pytesseract
import numpy as np
import datetime  

# Read the image file 84, 234, 54, 34, 61, 74 ,214
#not working 90,65,262
image = cv2.imread('./data/images/62.JPG')
# image = cv2.imread('./numberPlates/321.JPG')
# image = cv2.imread('324.JPG')
# image=cv2.resize(image,(600,400))
# Convert to Grayscale Image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image=cv2.bilateralFilter(gray_image,13,15,15)

# # kernel=np.array([
# # 	[1,0,0,0],
# # 	[0,1,0,0],
# # 	[0,0,1,0],
# # 	[0,0,0,1]
# # ])

# # filtered=cv2.filter2D(gray_image.copy,-1,kernel)

# # cv2.imshow("filtered",filtered)
# #Canny Edge Detection
canny_edge = cv2.Canny(gray_image, 170, 200)
# cv2.imshow("canny",canny_edge)

# Find contours based on Edges
contours, new  = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]

# cv2.drawContours(image,contours,-1,(239,230,0),2)

# Initialize license Plate contour and x,y coordinates
contour_with_license_plate = None
license_plate = None
x = None
y = None
w = None
h = None

f=0 #set to 1 if lisence plate is detected 
# Find the contour with 4 potential corners and creat ROI around it
for contour in contours:
        # Find Perimeter of contour and it should be a closed contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
        if len(approx) == 4: #see whether it is a Rect
            contour_with_license_plate = approx
            x, y, w, h = cv2.boundingRect(contour)
            license_plate = gray_image[y:y + h, x:x + w]
            f=1

            break

# Removing Noise from the detected image, before sending to Tesseract
license_plate = cv2.bilateralFilter(license_plate, 11, 17, 17)
(thresh, license_plate) = cv2.threshold(license_plate, 150, 180, cv2.THRESH_BINARY)

# license_plate = cv2.resize(license_plate, (90,50),interpolation = cv2.INTER_NEAREST) 

# kernel2=np.array([
# 	[0,1,0],
# 	[0,1,0],
# 	[0,1,0]
# ])

# license_plate=cv2.filter2D(license_plate,-1,kernel2)
#Text Recognition
text = pytesseract.image_to_string(license_plate, config='--oem 3 --psm 11 tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
#Draw License Plate and write the Text
image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2) 
# image = cv2.putText(image, text, (x-100,y-50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 6, cv2.LINE_AA)

print("License Plate :", text)

cv2.imshow("license_plate",license_plate)
cv2.imshow("License Plate Detection",image)

today = datetime.datetime.now()
day=today.day
text=text.rstrip()
for i in text[::-1]:
    if i.isdigit():
        car=int(i)
        break
print(today)

if day%2==0:
    if car%2==0:
        print("Car allowed")
    else:
        print("Car not allowed")
else:

    if car%2==1:
        print("Car allowed")
    else:
        print("Car not allowed")
cv2.waitKey()