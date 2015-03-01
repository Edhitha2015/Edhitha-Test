import Tkinter, Tkconstants, tkFileDialog
import sdwithui, blobandbackproject1, colorwithui, gps
from PIL import Image

class TkFileDialogExample(Tkinter.Frame):
	def __init__(self, root):

		Tkinter.Frame.__init__(self, root)

		# options for buttons
		button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

		# define buttons
		Tkinter.Button(self, text='shapedetect', command=self.shapedetect).pack(**button_opt)
		Tkinter.Button(self, text='blobextractandbackproject', command=self.blobextractandbackproject).pack(**button_opt)
		Tkinter.Button(self, text='colordetect', command=self.colordetect).pack(**button_opt)
		Tkinter.Button(self, text='gps', command=self.gps).pack(**button_opt)
		#Tkinter.Button(self, text='askopenfilenames', command=self.askopenfilenames).pack(**button_opt)

		# define options for opening or saving a file
		self.file_opt = options = {}
		options['defaultextension'] = '.txt'
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = 'C:\\'
		#options['initialfile'] = 'myfile.txt'
		options['parent'] = root
		options['title'] = 'This is a title'

		# This is only available on the Macintosh, and only when Navigation Services are installed.
		#options['message'] = 'message'

		# if you use the multiple file version of the module functions this option is set automatically.
		#options['multiple'] = 1

		# defining options for opening a directory
		self.dir_opt = options = {}
		options['initialdir'] = 'C:\\'
		options['mustexist'] = False
		options['parent'] = root
		options['title'] = 'This is a title'

	def shapedetect(self):

		"""Returns an opened file in read mode.
		This time the dialog just returns a filename and the file is opened by your own code.
		"""

		# get filename
		filename = tkFileDialog.askopenfilenames(**self.file_opt)
		print filename
		for f in filename:
			print f
			sdwithui.shapedetect(f)
		# open file on your own
		#if filename:
		# return open(filename, 'r')

	def blobextractandbackproject(self):
		filename = tkFileDialog.askopenfilenames(**self.file_opt)
		print filename
		for f in filename:
			print f
			blobandbackproject1.backproject(f)

	def colordetect(self):
		filename = tkFileDialog.askopenfilenames(**self.file_opt)
		print filename
		for f in filename:
			print f
			colorwithui.color(f)

	def gps(self):
		filename = tkFileDialog.askopenfilenames(**self.file_opt)
		print filename
		for f in filename:
			print f
			image = Image.open(f)
			print gps.latlon(image)

if __name__=='__main__':
  root = Tkinter.Tk()
  TkFileDialogExample(root).pack()
  root.mainloop()