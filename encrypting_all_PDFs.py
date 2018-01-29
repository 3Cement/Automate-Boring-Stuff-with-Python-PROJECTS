#! python3
# encrypting_all_PDFs.py - script that will go through every PDF in a folder
# and encrypt the PDFs using a provided password. 

import os, PyPDF2, time

def encryptingPDFs(password):
	start_time = time.time()
	for folderName, subfolders, filenames in os.walk('C:\\Users\\Daniel\\MyPythonScripts\\PDFPython'):
		print('The current folder is ' + folderName)

		for filename in filenames:
			if filename.endswith('.pdf'):
				pdfFile = open(filename, 'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
				pdfWriter = PyPDF2.PdfFileWriter()
				for pageNum in range(pdfReader.numPages):
					pdfWriter.addPage(pdfReader.getPage(pageNum))				
				pdfWriter.encrypt(password)
				resultPdf = open('encrypted_'+ filename, 'wb')
				pdfWriter.write(resultPdf)
				resultPdf.close()

	end_time = time.time()
	print("\n--- %s seconds ---" % round((end_time - start_time),2))

encryptingPDFs('myPass')

