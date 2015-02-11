import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
gCounter = 0
SIncrement = 0
fIncrement = 0

# add nulls, when num doesn`t composed of six digits
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

# get sum of all digits in num
def getSum(num):
	sum = 0
	for i in str(num):
		sum = sum + int(i)
	return sum

# create cycle, whick iterate max-min times
for i in range( max(x,y) - min(x,y) ):
	# fHalf and sHalf - first and second halfs of min number
	fHalf = int(makeStringWithNull(min(x,y))[0:3]) + fIncrement
	sHalf = int(makeStringWithNull(min(x,y))[3:]) + SIncrement
	print "Second Half"
	print sHalf
	print "SIncrement"
	print SIncrement
	# if we found that lucky num SIncrement counter
	if(getSum(fHalf) == getSum(sHalf)):
		gCounter = gCounter + 1
	# gradually increase second half of number for 1 and if it is over 999 SIncrement firstHalf by 1
	# for example if we have 223999, next num in cycle will be 224000


	# need to make sHalf null after this IF!!!!!!!!!!
	



	if (sHalf == 999):
		fIncrement = fIncrement + 1
		SIncrement = 0
	# increse second half by 1
	SIncrement = SIncrement + 1

print gCounter+1