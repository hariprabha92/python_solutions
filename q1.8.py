def maxcount(l):
#	a=dict()
	count=0
	c=0
	for i in l:
		c=0
		for j in l:
			if i==j :
				c+=1
			else:
				pass
		if c > count:
			count=c
		else:
			pass

	return count	
	
a=maxcount([1,17,31,17,22,17])
print a
b=maxcount(["the","higher","you","climb","the","further","you","fall"])
print b
c=maxcount([1,17,31,17,22,17])
print c
d=maxcount(["the","higher","you","climb","the","further","you","fall"])
print d

