import sys

str = "I canT DAnCE i CANt TAlK Hey"
key = "aaaaabbbbbabbbaabbababbaaababaab"
alphabet = "abcdefghijklmnopqrstuvwxyz"

#insert spaces after every 5 characterss
def insert_newlines(string, every=5):
    lines = []
    for i in xrange(0, len(string), every):
        lines.append(string[i:i+every])
    return ' '.join(lines)

#recognise lower or uppercase and replace to a or b
def subst(char):
    if(char.lower() == char):
        return 'a'
    else:
        return 'b'

# main function
def decoder(stringpar):
    temp = stringpar
    temp = temp.replace(" ", "")
    lenstr = len(temp)
    codeab = ''
    #remove last characters
    for i in range(10):
        if(lenstr%5 != 0):
            lenstr = lenstr - 1
            temp = temp[:-1]

    temp = insert_newlines(temp,5)

    #coding all string to a and b

    for i in temp:
        if(i != " "):
            codeab += subst(i)
        else:
            codeab += " "
            
    temp = codeab
    return temp

print decoder(str)