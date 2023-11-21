inputStr = input("Enter String")
outputStr1 = ""
outputStr2 = ""

for c in inputStr:
    outputStr1 += "{:08b}".format(ord(c))
    outputStr2 += bin(ord(c))
print(outputStr1)
print(outputStr2)
# print("Binary value of 10:",bin(-10))
# print("{:08b}".format(37))
