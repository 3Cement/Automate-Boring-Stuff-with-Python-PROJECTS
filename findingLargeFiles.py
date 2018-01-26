#! python3 
# findLargeFiles.py - The program that walks through a folder tree and searches
# for exceptionally large files or folder, ones that have a file size of more
# than that you choose (for example 1000MB). And print these files with their
# absolute path to the screen.

import os, operator, time
# Choose the folder and file sizes you are looking for.
def findLargeFiles(folder, sizeMB):
	start_time = time.time()
	# sizeMB - size of file in MB
	folder = os.path.abspath(folder)
	fileSize = sizeMB*1048576 

	filesNumber = 0
	largeFiles = []

	# Walk through a folder tree and searcehs for large files
	print('Looking for files bigger than %sMB... in %s' % (sizeMB, folder))
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			size = os.path.getsize(os.path.join(foldername, filename))
			sizeInMB = size/1048576
			if size >= fileSize:
				filesNumber = filesNumber + 1
				filePath = os.path.join(foldername, filename)
				print('\n'+filePath)
				print(filename)
				print(round(sizeInMB,2))
				largeFiles.append((round(sizeInMB,2), filename))

	print('\nFound %s files larger than %sMB!' % (filesNumber, sizeMB))
	#print(largeFiles)

	largeFiles.sort(key=lambda s: s[0])

	for file in largeFiles:
		print(file)	
	end_time = time.time()
	print("\n--- %s seconds ---" % round((end_time - start_time),2))

findLargeFiles('C:\\Users\\Daniel\\Downloads', 1000)
