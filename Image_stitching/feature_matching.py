import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob


MIN_MATCH_COUNT = 10

a1=cv2.imread("Data/1/19.jpg",cv2.IMREAD_GRAYSCALE)
a2=cv2.imread("Data/1/54.jpg",cv2.IMREAD_GRAYSCALE)

img1=cv2.resize(a1,(640,480))
img2=cv2.resize(a2,(640,480))

#img1=cv2.rotate(a1, cv2.ROTATE_90_CLOCKWISE)
#img2=cv2.rotate(a2, cv2.ROTATE_90_CLOCKWISE)

orb=cv2.ORB_create()


kp1,des1=orb.detectAndCompute(img1,None)
kp2,des2=orb.detectAndCompute(img1,None)


bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

matches=bf.match(des1,des2)
matches=sorted(matches,key=lambda x:x.distance)
matching_results=cv2.drawMatches(img1, kp1, img2, kp2, matches, None,flags=2)




cv2.imshow("1",img1)
cv2.imshow("2",img2)
plt.imshow(matching_results),plt.show()
cv2.imshow("Matched",matching_results)
cv2.waitKey(0)
