from math import factorial
total = 0
for i in xrange(10,1000000):
	if i == sum(map(factorial, map(int,str(i)))):
		total += i
print total
