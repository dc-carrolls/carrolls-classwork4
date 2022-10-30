numbers = []
for _ in range(6):
    numbers.append(int(input("enter num:")))
#next _
total = 0
for index in range(5,-1,-1): #For index = 5 to 0 step -1
    print(numbers[index])
    total = total + numbers[index]
#next index

print('total', total)
print("average", total//6)
    