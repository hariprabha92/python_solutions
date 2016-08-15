import os
import shutil
def rmfiles():
	dest='./files'
	for filename in os.listdir('.'):
		if (filename.endswith('.txt')) |  (filename.endswith('.pdf')):
			shutil.move(filename,dest)
		else:
			continue
rmfiles()
       
