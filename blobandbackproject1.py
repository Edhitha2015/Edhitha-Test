import cv2
import numpy as np
from decimal import *
import Tkinter, Tkconstants, tkFileDialog
'''class TkFileDialogExample(Tkinter.Frame):
	def __init__(self, root):

		Tkinter.Frame.__init__(self, root)

		# options for buttons
		button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

		# define buttons
		Tkinter.Button(self, text='Blobandbackproject1', command=self.askopenfilenames).pack(**button_opt)

		# define options for opening or saving a file
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\'
		#options['initialfile'] = 'myfile.txt'
		options['parent'] = root
		options['title'] = 'Blobandbackproject1'

		# This is only available on the Macintosh, and only when Navigation Services are installed.
		#options['message'] = 'message'

		# if you use the multiple file version of the module functions this option is set automatically.
		#options['multiple'] = 1

		# defining options for opening a directory
		self.dir_opt = options = {}
		options['initialdir'] = 'C:\\'
		options['mustexist'] = False
		options['parent'] = root
		options['title'] = 'Blobandbackproject1'

	def askopenfilenames(self):

		"""Returns an opened file in read mode.
		This time the dialog just returns a filename and the file is opened by your own code.
		"""

		# get filename
		filename = tkFileDialog.askopenfilenames(**self.file_opt)
		print filename
		for f in filename:
			print f
			backproject(f)
		# open file on your own
		#if filename:
		# return open(filename, 'r')'''

def extractblob(im):
	#print im.shape
	imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,0,255,0)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	z=0;
	for cnt in contours:
   	  	
                if cv2.contourArea(cnt)>100 and cv2.contourArea(cnt)<10000:
			#print cv2.contourArea(cnt)
     			cv2.drawContours(im,[cnt],0,(0,255,0),3)
     			x,y,w,h = cv2.boundingRect(cnt)
			rect=cv2.minAreaRect(cnt)
			#print rect
			box=cv2.cv.BoxPoints(rect)
			box=np.int0(box)
			#print box
			#cv2.drawContours(im,[box],0,(0,0,255),2)
     			cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
			print "w=%d h=%d"%(w,h)
			c=Decimal(rect[1][0])/Decimal(rect[1][1])
			d=Decimal(rect[1][1])/Decimal(rect[1][0])
			#print c
			#print d
			if c>Decimal(4)/Decimal(2.5) or d>Decimal(4)/Decimal(2.5):
			   continue
     			crop=im[y:y+h,x:x+w]
     			cv2.imwrite("procima/crop%d.jpg"%(z),crop)
     			cv2.imshow("crop%d"%(z),crop);
     			z=z+1;
        cv2.imwrite("procima/windowtitled.JPG", im)
	cv2.imshow("hello",im)
	cv2.waitKey(0)

def backproject(filename):
        im = cv2.imread(filename)
	#im = cv2.resize(im, None, fx = 0.25, fy = 0.25)
	
	#image => hsv, hist
	hsv = cv2.cvtColor( im, cv2.COLOR_BGR2HSV)
	#cv2.imshow("hsv", hsv)
	imHist = cv2.calcHist([hsv], [0,1], None, [180, 256],[0,180,0,256])

	bckP = cv2.calcBackProject([hsv], [0,1], imHist,[0,180,0,256], 1)
	#cv2.imshow("bp", bckP)
	kernel = cv2.getStructuringElement( cv2.MORPH_ELLIPSE, (3,3))
	closing = cv2.morphologyEx(bckP, cv2.MORPH_CLOSE, kernel)
	#cv2.imshow("eroded", closing)

	##dst = cv2.filter2D(closing, -1,kernel)
	##cv2.imshow('2d', dst)

	ret,thresh = cv2.threshold(closing, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	#cv2.imshow("thresh", thresh)

	fm1 =  cv2.merge((thresh,thresh,thresh))
	res1 = cv2.bitwise_and(im, fm1, mask = None)# mask here has no significance
        #cv2.imshow("first and", res1)
	
	#make (lower bound) G= 180 for proper target. G= 90 makes its edges disappear a leeettle
	mask = cv2.inRange(hsv, np.array([5,90,50], dtype = np.uint8), np.array([49,255,205], dtype = np.uint8)) 
	mask_inv = cv2.bitwise_not(mask)
	res = cv2.bitwise_and(res1, res1, mask = mask_inv)
	cv2.imwrite("procima/final.jpg", res)
	kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	res=cv2.erode(res,kernel,iterations=1)
	cv2.imwrite("procima/bckP.JPG",res)
	extractblob(res)

	
'''if __name__=='__main__':
  root = Tkinter.Tk()
  TkFileDialogExample(root).pack()
  root.mainloop()'''
	

