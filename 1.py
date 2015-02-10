import sys

str = sys.argv[1]
lh = 0
rh = 0
count = len(str)
i = 0


for i in str:
	if ( i == ')'):
		lh = lh + 1
	else:
		rh = rh + 1


for i in range(20):
	if (str[0] == ')' or str[-1] == '(' or len(str) % 2 != 0 or (lh != rh)):
		print "NO"
		break

	str = str.replace('()', "")
	if (str == ""):
		print "YES"
		break
	
