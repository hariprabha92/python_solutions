import shutil, os, re
def rmdate():
	datePattern = re.compile(r"""^(.*?) ((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
	for amrfilename in os.listdir('.'):
		mo = datePattern.search(amrfilename)
		if mo == None:
			continue
		beforePart = mo.group(1)
		monthPart  = mo.group(2)
		dayPart    = mo.group(4)
		yearPart   = mo.group(6)
		afterPart  = mo.group(8)

		euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart +afterPart
		absWorkingDir = os.path.abspath('.')
		amrfilename = os.path.join(absWorkingDir, amrfilename)
		euroFilename = os.path.join(absWorkingDir, euroFilename)

    
		print('Renaming "%s" to "%s"...' % (amrfilename, euroFilename))
rmdate()
