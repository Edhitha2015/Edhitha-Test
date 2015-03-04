# name all the images from img1..... imgn in the folder /Edhitha/imF0
# if target is spotted, press 's' to save to imgF1
# missed an image with a target? Want to recheck? press 'p' to view the previous image

import cv2
import numpy as np
import os.path
path = 'test-images/'
nxtPath = 'blobby/'
# numFiles = number of files in imgF0
numFiles = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])

print numFiles

z=0
if (numFiles):
	for c in range(1, numFiles+1):
	
		print c
		imPath = path+'img%d.jpg'%(c)
		im = cv2.imread(imPath)
		im = cv2.resize(im,None, fx = 0.25, fy = 0.25)
		# display resized image 
		cv2.imshow("img%d"%(c), im)
		k = cv2.waitKey(0)
		if k == ord('p'):
			cv2.destroyWindow("img%d"%(c))
			# raise a flag upon a request to go back, iedisplay previous image
			flagP = 1
			print "a%d"%(c)
		# press 's' to save image to imF0 folder
		elif k == ord('s'):
			# code for when 'p' is pressed & it has to be saved
			# numNxtFile = number of files in imgF1
			numNxtFile = len([f for f in os.listdir(nxtPath)
       					  if os.path.isfile(os.path.join(nxtPath, f))])
			# saving non resized image
			cv2.imwrite(nxtPath+'im%d.jpg'%(numNxtFile+1),cv2.imread(imPath)) 
			cv2.destroyWindow("img%d"%(c))
		# press any button except 's' and 'p' to view next image
		else:
			print "0"
			cv2.destroyWindow("img%d"%(c))
'''
imPath = path+'img%d.jpg'%(c)

im = cv2.imread(imPath)
cv2.imshow("img%d"%(c), im)
cv2.waitKey(0)'''
