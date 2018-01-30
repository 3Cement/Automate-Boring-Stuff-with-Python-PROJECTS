#! python3
# PDFPassBreaker.py - Program that will decrypt the PDF by trying every possible English
# word until it finds one that works.

import os, PyPDF2, time, logging
logging.basicConfig(level=logging.DEBUG)

def decryptingPDF(filename):
	start_time = time.time()
	pdfFile = open(filename, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	if not pdfReader.isEncrypted:
		logging.warning("The file: " + str(filename) + " is not encrypted.")
		contiune
	try:
		with open("dictionary.txt") as file:
			wList = file.read().splitlines()
			for word in wList:
				password = word
				try:
					pdfReader.decrypt(password)
					pdfWriter = PyPDF2.PdfFileWriter()
					for pageNum in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(pageNum))
					logging.info("File: " + str(filename) + " was successfully decrypted.")
					pdfReader.getPage(0)
					resultPdf = open('decrypted_' + filename, 'wb')
					pdfWriter.write(resultPdf)
					resultPdf.close()
					pdfFile.close()
					logging.info('Done! The found password is: '+ password)
					break
				except Exception as err:
					logging.error(password + " is wrong. File decryption failed: " + str(err))
	except Exception as err:
		logging.error("File decryption failed: " + str(err))

	end_time = time.time()
	logging.info("\n--- %s seconds ---" % round((end_time - start_time),2))

decryptingPDF('MyFile')
