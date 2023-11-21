import random
candidates = ["A","B","C","D"]


stackA = ["X" for _ in range(100)]
stackB = []
stackC = []

#Generate stackA data
for i in range(0,41):
    done = False
    while not done:
        rnd=random.randint(0,99)
        #rnd=i
        if stackA[rnd] == "X":
            stackA[rnd] = "B"
            done = True

for i in range(100):
    if stackA[i] == "X":
        stackA[i] = random.choice(candidates[1:])
    

print(stackA)

#print(stackA[-1]) #peek

#print("A:",stackA.count("A"))

def processStream(stack1):
    m = ""
    i = 0
    while len(stack1) != 0:
        if i == 0: 
            m = stack1.pop()
            i = 1
        elif m == stack1.pop():
            i += 1
        else:
            i -= 1
        #end if
    #end while
    return m
#end function



def processStack(stack1, stack2, stack3):
    while len(stack1) != 0:
        if len(stack2) != 0: 
            if stack1[-1] == stack2[-1]:
                stack2.append(stack1.pop())
            else:
                stack3.append(stack1.pop())
                stack3.append(stack2.pop())
            #end if
        else:
            stack2.append(stack1.pop())
        #end if

    if len(stack2) != 0:
        return stack2[-1]
    else:
        return "X"
#end function


# result = processStack(stackA,stackB,stackC)
# if result == "X":
#     print("No majority")
# else:
#     print(result)
#     result = processStack(stackC,stackB,stackA)
#     if result == "X":
#         print("No majority")
#     else:
#         print(result)

print(processStream(stackA))
        


# while len(stacks[1]) != 0 and len(stacks[2]) != 0:
#     stacks[1].pop()
#     stacks[2].pop()

# if len(stacks[1]) != 0:
#     print("A")
# else:
#     print("B")



