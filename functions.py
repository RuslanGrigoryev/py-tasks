def removeFirstNum(num):
    if(num > 9999):
        num = str(num)
        return int(num[2:])
    else:
        if(num > 999):
            num = str(num)
            return int(num[1:])

def getSum(num):
    sum = 0
    for i in str(num):
        sum = sum + int(i)
    return sum

print removeFirstNum(200988)
print getSum(removeFirstNum(2001))