def myreverse(l):
  if(l==[]):
    return(l)
  else:
    return [l[-1]] + myreverse(l[:-1])
	
a=myreverse([1,2,3,4,5])
print a
