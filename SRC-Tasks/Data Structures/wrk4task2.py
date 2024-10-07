class Stack:
    def __init__(self,size) -> None:
        self.maxSize = size
        self.data = ['' for _ in range(size)]
        self.sp = -1
    #end constructor

    def size(self):
        return self.sp + 1

    def isFull(self):
        return self.size() == self.maxSize
    
    def isEmpty(self):
        return self.sp == -1

    def push(self,item):
        if self.isFull():
            print('Is Full')
        else:
            self.sp += 1
            self.data[self.sp] = item
        #end if
    #end procedure

    def pop(self):
        if self.isEmpty():
            print('Is empty')
        else:
            temp = self.sp
            self.sp -= 1
            return self.data[temp]
        #endif
    #end function

    def peek(self):
        if not self.isEmoty():
            return self.data[self.sp]
        #endif
    #end function
          
#end class

myString = input ('Please enter a word or phrase to be tested: ')
numChars = len(myString)
palList = []
s = Stack(numChars)
s.pop()
for c in myString:
    s.push(c)

s.push('x')
print(s.data)
while not s.isEmpty():
    palList.append(s.pop())

print(''.join(palList))

if myString == ''.join(palList):
    print('IS palindrome')
else:
    print('is not palindrome')
