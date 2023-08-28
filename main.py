import cv2
import numpy as np


kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "img.png"
img = cv2.imread(path)
print(img.shape)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(imgGray.shape)
imgBlur = cv2.GaussianBlur(imgGray,(9,9),20)
imgCanny = cv2.Canny(imgBlur,100,200)
imgDilation = cv2.dilate(imgCanny,kernel , iterations = 5)
imgEroded = cv2.erode(imgDilation,kernel,iterations=1)


cv2.imshow("img",imgGray)
#cv2.imshow("GrayScale",imgGray)
cv2.imshow("Img Blur",imgBlur)
#cv2.imshow("Img Canny",imgCanny)
cv2.imshow("Img Dilation",imgDilation)
cv2.imshow("Img Erosion",imgEroded)
cv2.waitKey(0)
