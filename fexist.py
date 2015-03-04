import os 
import cv2
from time import sleep 
i=0
#path = "From_Camera/img{a}.jpg".format(a = str(i))
#print path
#jpg = "jpg"
while(True):
	path = "From_Camera/img" + str(i) + ".jpg" 
	print path
	if os.path.isfile(path):
		print "yes"
		# Do whatever you want this makes it non-vulnerable to updates/dynamic pushes. 
	else:
		sleep(1)
		i = i-1
	i=i+1

