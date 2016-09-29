import math
def squarefree(l):
	f=1
	d=l
	l=l//2
	for i in range(2,l):
		if d%i == 0:
			if (math.sqrt(i)-int(math.sqrt(i))):
				return False
		else:
			pass
	if f==1:
		return True
	else:
		pass
#a=squarefree(1001)
a=squarefree(57768232)
print a			

		
