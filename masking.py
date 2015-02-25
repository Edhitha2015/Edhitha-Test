import cv2
import numpy as np

im = cv2.imread("blobby/crop0.jpg")
#im = cv2.resize(im, None, fx = 0.25, fy = 0.25)
print im.shape
hsv = cv2.cvtColor( im, cv2.COLOR_BGR2HSV)
#yuv = cv2.cvtColor( im, cv2.COLOR_RGB2YUV)
hsv = cv2.medianBlur(hsv, 5)


mask = cv2.inRange(hsv, np.array([50,100,100], dtype = np.uint8), np.array([70,255,255], dtype = np.uint8))
mask_inv = cv2.bitwise_not(mask)
res= cv2.bitwise_and(im, im, mask = mask_inv)

cv2.imwrite('blobby/final.jpg', res)
cv2.imshow('hsv', hsv)
cv2.imshow('mask', mask)
cv2.imshow('final', res)
cv2.waitKey(0)
