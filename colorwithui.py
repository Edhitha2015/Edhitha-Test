import numpy as np
import cv2
import Tkinter, Tkconstants, tkFileDialog
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import utils
import webcolors1

'''def shapedetect(filename):
	
	img = cv2.imread(filename)
	gray = cv2.imread(filename,0)
	graycv = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # whats the difference between this and the previous command ? 

	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(gray,kernel,iterations = 1)

	ret,thresh = cv2.threshold(erosion,127,255,1)

	contours,h = cv2.findContours(thresh,1,2)
	print len(contours)
	for cnt in contours:
	    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
	    print len(approx)
	    if len(approx)==5:
	        print "pentagon"
	        cv2.drawContours(img,[cnt],0,255,-1)
	    elif len(approx)==3:
	        print "triangle"
	        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
	    elif len(approx)==4:
	        print "square"
	        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
	    elif len(approx) == 9:
	        print "half-circle"
	        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
	    elif len(approx) == 11:
		print "star"
	    elif len(approx) > 15:
	        print "circle"
	        cv2.drawContours(img,[cnt],0,(0,255,255),-1)
	cv2.imshow('graycv', graycv)
	cv2.imshow('erode', erosion)
	cv2.imshow('gray',gray)
	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
'''
def color(filename):
	image = cv2.imread(filename)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	plt.figure()
	plt.axis("off")
	plt.imshow(image)
	image = image.reshape((image.shape[0] * image.shape[1], 3))
	clt = KMeans(n_clusters = 5)
	clt.fit(image)

	hist = utils.centroid_histogram(clt)

	bar = utils.plot_colors(hist, clt.cluster_centers_)

	plt.figure()
	plt.axis("off")
	plt.imshow(bar)
	plt.show()

class TkFileDialogExample(Tkinter.Frame):
	def __init__(self, root):

		Tkinter.Frame.__init__(self, root)

		# options for buttons
		button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

		# define buttons
		Tkinter.Button(self, text='color.py', command=self.askopenfilenames).pack(**button_opt)

		# define options for opening or saving a file
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\'
		#options['initialfile'] = 'myfile.txt'
		options['parent'] = root
		options['title'] = 'Finding the color'

		# This is only available on the Macintosh, and only when Navigation Services are installed.
		#options['message'] = 'message'

		# if you use the multiple file version of the module functions this option is set automatically.
		#options['multiple'] = 1

		# defining options for opening a directory
		self.dir_opt = options = {}
		options['initialdir'] = 'C:\\'
		options['mustexist'] = False
		options['parent'] = root
		options['title'] = 'Finding the color'

	def askopenfilenames(self):

		"""Returns an opened file in read mode.
		This time the dialog just returns a filename and the file is opened by your own code.
		"""

		# get filename
		filename = tkFileDialog.askopenfilenames(**self.file_opt)
		print filename
		for f in filename:
			print f
			color(f)
		# open file on your own
		#if filename:
		# return open(filename, 'r')

if __name__=='__main__':
  root = Tkinter.Tk()
  TkFileDialogExample(root).pack()
  root.mainloop()