def mypalindrome(l):
  if(l==[] or len(l) == 1):
    return(True)
  else:
    return (l[-1]==l[0] and  mypalindrome(l[1:-1]))
a=mypalindrome([13,14,13])
print a
s=mypalindrome([22,16,16,22])
print s
b=mypalindrome([13,12,12])
print b
h=mypalindrome([12,22,12,22])
print h
d=mypalindrome([14,13,14])
print d
f=mypalindrome([2,4,4,2])
print f
g=mypalindrome([2,3])
print g
t=mypalindrome([32,32,12,32,43])
print t
