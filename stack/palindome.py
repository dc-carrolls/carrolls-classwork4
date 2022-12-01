myString = input("Please enter a word or phrase to be tested: ").upper()
s = ""
stack = []
for c in myString:
    if 64 < ord(c) < 91: 
        s = s + c
        stack.append(c) #push
    #end if 
#next c

newString = ""
for _ in range(len(stack)):
    newString = newString + stack.pop() #pop
#next _

if s == newString:
    print("Palindrome")
else:
    print("not palindrome")
#end if






