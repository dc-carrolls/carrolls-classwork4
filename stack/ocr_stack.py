import random
stack_size = 10
stack_data = [random.randint(1,100) for _ in range(stack_size)]

sp = -1

def stackSize():
    global sp
    return sp + 1

def isFull():
    global sp
    global stack_size
    if sp < stack_size-1:
        return False
    else:
        return True
    #endif
#end function

def isEmpty():
    global sp
    if sp == -1:
        return True
    else:
        return False
    #endif
#end function



def stack_push(item,stack_data):
    global sp
    if isFull():
        print("Stack is full")
    else:
        sp = sp + 1
        stack_data[sp]=item
    #endif
#end procedure

def stack_pop(stack_data):
    global sp
    if isEmpty():
        print("stack is empty")
    else:
        tmp = stack_data[sp]
        sp = sp - 1    
        return tmp    
    #endif
    
#end function
        
print(stack_data)

print(stack_pop(stack_data))

data = 1
while not isFull():
    stack_push(data,stack_data)
    data = data + 1
    print("stack size:",stackSize())
#endwhile

stack_push(11,stack_data)
print("stack size:",stackSize())

print(stack_data)


print(stack_pop(stack_data))
print("stack size:",stackSize())