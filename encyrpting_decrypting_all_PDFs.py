#! python3
# encyrpting_decrypting_all_PDFs.py - script that will go through every PDF in a folder
# and encrypt the PDFs using a provided password. Then with decryptingPDFs will decrypt all files.

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
				logging.info('Reading file: ' + str(file))
				pdfFile = open(filename, 'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
				if not pdfReader.isEncrypted:
					pdfWriter = PyPDF2.PdfFileWriter()
					# Copy every page
					for pageNum in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(pageNum))	
					# Encrypt each PDF file			
					pdfWriter.encrypt(password)
					logging.info("File " + str(file) + " has been successfully encrypted.")
					# Save file
					name = (os.path.basename(filename)).split(".")[0]
					newName = os.path.join(foldername, "encrypted_" + name + ".pdf")
					newName = os.path.abspath(newName)
					resultPdf = open(newName, 'wb')
					pdfWriter.write(resultPdf)
					printedName = (os.path.basename(newName)).split(".")[0] +'.pdf'
					logging.info("File has been renamed to: " + str(printedName))
					resultPdf.close()
					pdfFile.close()

	end_time = time.time()
	print("\n--- %s seconds ---" % round((end_time - start_time),2))

def decryptingPDFs(password):
	start_time = time.time()
	logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

	# Loop trhough all pdfs
	for foldername, subfolders, files in os.walk("."):
		for file in files:
			if file.endswith(".pdf"):
				# Decrypt PDF if is encrypted
				filename = os.path.join(foldername, file)
				filename = os.path.abspath(filename)
				fileObj = open(filename, "rb")
				pdfReader = PyPDF2.PdfFileReader(fileObj)
				if not pdfReader.isEncrypted:
					logging.warning("The file: " + str(file) + " is not encrypted.")
					continue
				try:
					pdfReader.decrypt(password)
					pdfWriter = PyPDF2.PdfFileWriter()
					for pageNum in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(pageNum))
					logging.info("File: " + str(file) + " was successfully decrypted.")
					name = (os.path.basename(file)).split(".")[0]
					newName = os.path.join(foldername, "decrypted_" + name + ".pdf")
					newName = os.path.abspath(newName)
					resultPdf = open(newName, 'wb')
					pdfWriter.write(resultPdf)
					printedName = (os.path.basename(newName)).split(".")[0] +'.pdf'
					logging.info("File has been renamed to: " + str(printedName))
					resultPdf.close()
					fileObj.close()
				except Exception as err:
					logging.error("File decryption failed: " + str(err))

	end_time = time.time()
	print("\n--- %s seconds ---" % round((end_time - start_time),2))

#encryptingPDFs('kiki')
#decryptingPDFs('kiki')
