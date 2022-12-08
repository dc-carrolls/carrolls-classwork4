numbers = [0 for _ in range(6)]
print(numbers)
for index in range(6):
    numbers[index] =int(input("enter num:"))
#next index
total = 0
for index in range(5,-1,-1): #For index = 5 to 0 step -1
    print(numbers[index])
    total = total + numbers[index]
#next index

print('total', total)
print("average", total//6)
    