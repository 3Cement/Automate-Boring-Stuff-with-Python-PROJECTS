#! python3
# encrypting_all_PDFs2.py - script that will go through every PDF in a folder
# and encrypt the PDFs using a provided password. 

import os, PyPDF2, time, logging

def encryptingPDFs(password):
	start_time = time.time()
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

	for foldername, subfolders, filenames in os.walk('.'):
		print('The current folder is ' + foldername)

		for file in filenames:
			# Finds PDF files
			if file.endswith('.pdf'):
				filename = os.path.abspath(os.path.join(foldername, file))
				logging.info('Reading file: ' + str(filename))
				pdfFile = open(filename, 'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
				if not pdfReader.isEncrypted:
					pdfWriter = PyPDF2.PdfFileWriter()
					# Copy every page
					for pageNum in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(pageNum))	
					# Encrypt each PDF file			
					pdfWriter.encrypt(password)
					logging.info("File " + str(filename) + " has been successfully encrypted")
					# Save file
					name = (os.path.basename(filename)).split(".")[0]
					newName = os.path.join(foldername, "encrypted_" + name + ".pdf")
					newName = os.path.abspath(newName)
					resultPdf = open(newName, 'wb')
					pdfWriter.write(resultPdf)
					logging.info("File has been renamed to: " + str(newName))
					resultPdf.close()
					pdfFile.close()

	end_time = time.time()
	print("\n--- %s seconds ---" % round((end_time - start_time),2))

encryptingPDFs('somePassword')

