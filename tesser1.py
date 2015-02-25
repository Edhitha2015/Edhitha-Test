import tesseract

api = tesseract.TessBaseAPI()
#api.Init(".","eng",tesseract.OEM_DEFAULT)
api.Init("/usr/share/tesseract-ocr/","eng",tesseract.OEM_DEFAULT)

api.SetVariable("tessedit_char_whitelist", "!@#$%^&*()<>?/{}[]+=_-,.;:~`""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#api.SetPageSegMode(tesseract.PSM_AUTO) #for euro.txt, i.e for a paragraph of text
#api.SetPageSegMode(tesseract.PSM_SINGLE_BLOCK)
api.SetPageSegMode(tesseract.PSM_SINGLE_CHAR) #for A.png/.jpg etc.

mImgFile = "/home/praneeta/Downloads/Pictures/g.jpg"
mBuffer=open(mImgFile,"rb").read()
result = tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
print "result(ProcessPagesBuffer)=", result
if not result:
	result = 'NA'
dumpFilePath = "./tesseractDump.txt"
fileDump = open(dumpFilePath,'a+')
fileDump.write("\n Letter is "+result)



