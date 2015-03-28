# import cv as cv2
# from qrtools import qr
# import numpy as np

# def rotateImage(image, angle):
#   image_center = tuple(np.array(image.shape)/2)
#   rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
#   result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_LINEAR)
#   return resultimport numpy as np


# im=cv2.imread("qr1.jpg")
# s=None
# if myCode.decode():
	
from sys import argv
import zbar
import Image
import cv2
import easygui as eg


# class DetectQRCode(object):

#     @classmethod

filetype = [["*.jpg", "*.jpeg", "JPEG files"] ,"*.png"]
loc=eg.fileopenbox(msg='Select a QR Image', title='Select Image', default='*', filetypes=filetype, multiple=False)

def detect_qr():
        # create a reader
        scanner = zbar.ImageScanner()
        image=cv2.imread(loc)
        #print image
        # configure the reader
        scanner.parse_config('enable')

        # obtain image data
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY,dstCn=0)
        pil = Image.fromarray(gray)
        width, height = pil.size
        raw = pil.tostring()


        # wrap image data
        image = zbar.Image(width, height, 'Y800', raw)

        # scan the image for barcodes
        scanner.scan(image)

        # extract results
        for symbol in image:
            # do something useful with results
            if symbol.data == "None":
                return "Drone bevindt zich buiten het raster"
            else:
                return symbol.data
choices=["Write"]
qr=detect_qr()
eg.buttonbox("Output: \n"+qr,image=loc,choices=choices)

f = open('workfile.csv', 'a')
try:

	if(f):	
		s="QR,"+qr+"\n";
		f.write(s)
		eg.msgbox("Csv Written")
		f.close()
		f = open('workfile.csv', 'r')
		eg.msgbox("CSV File:\n"+f.read())
	else:
		eg.msgbox("Failed")
finally:
	f.close()


#eg.msgbox(image=loc,)
