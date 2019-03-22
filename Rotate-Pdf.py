#importing PyPDF2 module
import PyPDF2 

# rotation angle (Clockwise)  
_rotationAngle_ = 90        #As per requirement 
# Make sure the angle is a multiple of 90

# path of original PDF  
pdfPath = 'tkinter.pdf'       #As per requirement i.e. pdf to be rotated

# new pdf file name 
outputFile = 'out_file.pdf'  # You can specify full path name as well to choose a specific directory

# opening original pdf file as file object
pdfFileObj = open(pdfPath, 'rb') 

# creating a pdf Reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# creating a pdf writer obj for output pdf 
pdfWriter = PyPDF2.PdfFileWriter() 

# rotating each page 
for i in range(pdfReader.numPages): 
    # Rotating pages one by one 
    pageObj = pdfReader.getPage(i)          #Getting single page and saving it in pageObj 
    pageObj.rotateClockwise(_rotationAngle_)    # pageObj.rotateAntiClockwise(_angle_) for anticlockwise rotation
 
    # adding rotated page object to pdf writer 
    pdfWriter.addPage(pageObj)              #These pages are saved as buffer, and will be written in Output file in one go
      
# output pdf file object 
outFileObj = open(outputFile, 'wb') 
  
# writing rotated pages to new file 
pdfWriter.write(outFileObj) 
  
# closing the original pdf file object 
pdfFileObj.close() 
      
# closing the output pdf file object 
outFileObj.close() 