# importing required modules 
import PyPDF2 
  

# pdf files to merge, mention them in exact order you want to merge them 
pdfFiles = ['pdf1.pdf', 'pdf2.pdf', 'pdf3.pdf'] 
 
# output pdf file name 
mergedFile  = 'merged_file.pdf'
  
# creating pdf file merge object 
pdfMerge = PyPDF2.PdfFileMerger() 
  
# appending pdfs one by one 
for i in pdfFiles: 
    pdfMerge.append(open(i, 'rb'))       # Saving files in pdfMerger obj buffer
      
# writing all pdfs to the output file 
with open(mergedFile, 'wb') as obj:         # Opening file mergedFile as obj in binary write mode
    pdfMerge.write(obj) 