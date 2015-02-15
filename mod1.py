import sys

str = "I canT DAnCE i CANt TAlK Hey"
key = "aaaaabbbbbabbbaabbababbaaababaab"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def insert_newlines(string, every=5):
    lines = []
    for i in xrange(0, len(string), every):
        lines.append(string[i:i+every])
    return ' '.join(lines)

def decoder(stringpar):
    temp = stringpar
    temp = temp.replace(" ", "")
    lenstr = len(temp)
    # remove last characters
    for i in range(10):
        if(lenstr%5 != 0):
            lenstr = lenstr - 1
            temp = temp[:-1]

    temp = insert_newlines(temp,5)

    return temp

print decoder(str)