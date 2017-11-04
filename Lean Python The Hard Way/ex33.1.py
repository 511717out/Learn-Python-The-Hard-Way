# _*_ coding:utf-8 _*_

def while_loop(i,m,t):
   numbers = []
   while i < m:
	    numbers.append(i)
	    
	    i = i + t
	    print "Numbers now:",numbers
	    print "At the bottom i is %d" % i
   
   print "The numbers"
   for num in numbers:
      print num
	  
while_loop(0,6,1)