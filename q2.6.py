def sublist(l1,l2):
	l1=set(l1)
	l2=set(l2)
	j=l2-l1
	i=l2-j
	if i == l1:
		return True
	else:
		return False
#	j=list(j)
#	print j
#	a=''
#	b=''
#	for i in l1:
#		i=str(i)
		a+=i
#	for j in l2:
#		j=str(j)
#		b+=j
	return b.startswith(a)
a=sublist([2,2,5],[2,2,3,4,5])
print a
b=sublist([2,4,4],[2,2,3,4,5])
print b
c=sublist([2,2,3],[2,2,3,4,5])
print c
d=sublist([2,2,4],[2,2,3,4,5])
print d
e=sublist([1],[3,4,1,5,6])
print e
f=sublist([],[7,8,9])
print f
g=sublist([13],[])
print g

