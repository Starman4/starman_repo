import cv2
import numpy as np
from matplotlib import pyplot as plt

img1=cv2.imread("Data/12.jpg")
img2=cv2.imread("Data/13.jpg")

orb=cv2.SIFT_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)


matches = sorted(matches, key = lambda x:x.distance)

list_kp1 = []
list_kp2 = []

for mat in matches:

    img1_idx = mat.queryIdx
    img2_idx = mat.trainIdx

    (x1, y1) = kp1[img1_idx].pt
    (x2, y2) = kp2[img2_idx].pt

    list_kp1.append((x1, y1))
    list_kp2.append((x2, y2))

pts_src = np.array(list_kp1)
pts_dst = np.array(list_kp2)



H = cv2.findHomography(pts_src, pts_dst, cv2.RANSAC,5.0)

width=img1.shape[1]+img2.shape[1]
height=img1.shape[0]+img2.shape[0]

result=cv2.warpPerspective(img1, H[0], (width, height))
result[0:img2.shape[0], 0:img2.shape[1]] = img2


src=result
temp=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
thresh=cv2.threshold(temp,0,255,cv2.THRESH_BINARY)
b,g,r=cv2.split(src)
rgba=[b,g,r,thresh[1]]
dst=cv2.merge(rgba,4)


thresh = cv2.threshold(temp, 0, 255, cv2.THRESH_BINARY)[1]
x, y, w, h = cv2.boundingRect(thresh)
cropped__img = dst[y:y+h, x:x+w,:]

cv2.imwrite("Data/Out/field.png",cropped__img)





