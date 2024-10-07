class Stack:
    #private data as array of strings
    #private sp as integer
    def __init__(self,maxSize) -> None:
        self.maxSize = maxSize
        self.data = ["" for _ in range(maxSize)]
        self.sp = -1
    #end constructor


    #private function isFull()
    def isFull(self):
        return self.sp == self.maxSize - 1
    #end function
    

    #private function isEmpty()
    def isEmpty(self):
        return self.sp == -1


    #public procedure push(item)
    def push(self,item):
        if self.isFull():
            print("Stack is full")
        else:
            self.sp += 1
            self.data[self.sp] = item
        #end if
    #end procedure

    #public function pop() -> item
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            temp = self.sp
            self.sp -= 1
            return self.data[temp]
                
        #end if

    #public function peek() -> item
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.data[self.sp]
        #end if
    #end function

    #public function size() -> size
    def size(self):
        return self.sp + 1
    
    def __len__(self) -> int:
        return self.sp + 1

    
    def display(self) -> str:
        rStr = '\033[31m'
        i = self.maxSize - 1
        while i > - 1:
            if i == self.sp:
                rStr += '\033[32m'
            rStr += self.data[i] + '\n'
            i -= 1
        return rStr + '\033[0m'
    




s = Stack(5)
for c in "hello":
    s.push(c)

print(s.display())
print('len:',len(s))

s.push('s')
for item in range(3):
    print(s.pop())

print(s.display())
print('len:',len(s))

s.push('x')
print(s.display())
print('len:',len(s))