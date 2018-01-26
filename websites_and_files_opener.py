#! python3
# websitesOpener.py - Opens for us our most viewed websites and files automatically.

import requests, sys, webbrowser, bs4, os, time

start_time = time.time()

files_list = [
"C:\\Users\\JOHN\\Downloads\\xyz.xlsx",
"C:\\Users\\JOHN\\Downloads\\yyy.xlsx"
]

try:
	print('Openning list of files...')
	for file in files_list:
		file = os.startfile(file)
except Exception as exc:
	print('There was a problem: %s' % (exc))

link_list = [
"https://www.facebook.com/",
"https://www.instagram.com/",
"https://twitter.com/"
]

print('Openning list of websites...')
for link in link_list:
	webpage = webbrowser.open(link) 

end_time = time.time()
print("\n--- %s seconds ---" % round((end_time - start_time),2))
