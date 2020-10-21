import cv2
import pytesseract
import numpy as np
import datetime  
import scipy as sp
import scipy.ndimage


#Imfill algorithm credits:https://stackoverflow.com/questions/36294025/python-equivalent-to-matlab-funciton-imfill-for-grayscale/36333654
def flood_fill(test_array,h_max=255):
    input_array = np.copy(test_array) 
    el = sp.ndimage.generate_binary_structure(2,2).astype(np.int)
    inside_mask = sp.ndimage.binary_erosion(~np.isnan(input_array), structure=el)
    output_array = np.copy(input_array)
    output_array[inside_mask]=h_max
    output_old_array = np.copy(input_array)
    output_old_array.fill(0)   
    el = sp.ndimage.generate_binary_structure(2,1).astype(np.int)
    while not np.array_equal(output_old_array, output_array):
        output_old_array = np.copy(output_array)
        output_array = np.maximum(input_array,sp.ndimage.grey_erosion(output_array, size=(3,3), footprint=el))
    return output_array


# Read the image file 54,74
#not working 90,65,262
image = cv2.imread('./data/images/54.JPG')

image=cv2.resize(image,(300,300))

bla=np.zeros((300,300))
#preprocessing starts
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur=cv2.bilateralFilter(gray_image,13,15,15)

contrastEn = cv2.equalizeHist(blur)

kernel=np.ones((11,11))
opening = cv2.morphologyEx(contrastEn, cv2.MORPH_OPEN, kernel)

sub=cv2.subtract(contrastEn,opening)

# binarized=cv2.adaptiveThreshold(sub,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
ret2,binarized = cv2.threshold(sub,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) #otsu binarization

canny_edge = cv2.Canny(binarized,100,200)

kernel2=np.ones((2,2))
dilation = cv2.dilate(canny_edge,kernel2,iterations = 1)

imfill=flood_fill(canny_edge)

exactPlateStep1=cv2.morphologyEx(imfill, cv2.MORPH_OPEN, kernel)
exactPlateStep2=cv2.erode(imfill,kernel,iterations = 1)

#extra done
exact=cv2.morphologyEx(exactPlateStep2, cv2.MORPH_OPEN, kernel)

kernel3=np.ones((11,11))
exactDilation = cv2.dilate(exact,kernel3,iterations = 1)

#preprocessing ends
res1=np.hstack((gray_image,blur,contrastEn))
res2=np.hstack((opening,sub,binarized))
res3=np.hstack((canny_edge,dilation,imfill))
res4=np.hstack((exactPlateStep1,exactPlateStep2))

# cv2.imshow("stage1",res1)
# cv2.imshow("stage2",res2)
# cv2.imshow("stage3",res3)
# cv2.imshow("stage4",res4)
# cv2.imshow("result",exact)

# Find contours based on Edges
contours, new  = cv2.findContours(exactDilation.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours=sorted(contours, key = cv2.contourArea, reverse = True)[:30]

cv2.drawContours(image,contours,-1,(239,230,0),2)
cv2.imshow("contours",image)

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

licBlur=cv2.bilateralFilter(license_plate,13,15,15)

license_plate=licBlur

#Text Recognition
text = pytesseract.image_to_string(license_plate, config='--oem 3 --psm 11 tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
#Draw License Plate and write the Text
image = cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2) 
# image = cv2.putText(image, text, (x-100,y-50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 6, cv2.LINE_AA)

cv2.imshow("result",image)
cv2.imshow("license_plate",license_plate)

print("License Plate :", text)

today = datetime.datetime.now()
day=today.day
text=text.rstrip()
for i in text[::-1]:
    if i.isdigit():
        car=int(i)
        break
print(today)

# if day%2==0:
#     if car%2==0:
#         print("Car allowed")
#     else:
#         print("Car not allowed")
# else:

#     if car%2==1:
#         print("Car allowed")
#     else:
#         print("Car not allowed")
cv2.waitKey()