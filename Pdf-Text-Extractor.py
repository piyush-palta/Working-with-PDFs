# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('filename.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# printing number of pages in pdf file 
x=pdfReader.numPages 
  
file=open('file.txt','a+')
  
# creating a page object 
for i in range(x):
	pageObj = pdfReader.getPage(i) 
# extracting text from page 
	file.write(pageObj.extractText()) 
	file.write("\n")
file.close()  
# closing the pdf file object 
pdfFileObj.close()