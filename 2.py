import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
gCounter = 0
increment = 1

def makeStringWithNull(num):
	if (num < 9):
		num = "00000"+str(num)
	elif (num < 99):
		num = "0000"+str(num)
	elif (num < 999):
		num = "000"+str(num)
	elif (num < 9999):
		num = "00"+str(num)
	elif (num < 99999):
		num = "0"+str(num)
	else:
		num = str(num)
	return num

def getSum(num):
	sum = 0
	for i in str(num):
		sum = sum + int(i)
	return sum

for i in range( max(x,y) - min(x,y) ):
	fHalf = int(makeStringWithNull(min(x,y))[0:3])
	sHalf = int(makeStringWithNull(min(x,y))[3:])+increment
	if(getSum(fHalf) == getSum(sHalf)):
		gCounter = gCounter + 1
	
	if (sHalf == 999):
		fHalf = fHalf + 1
	print sHalf
	print fHalf
	increment = increment + 1

print gCounter+1