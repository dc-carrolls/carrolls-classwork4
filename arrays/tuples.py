from re import A


tuple1 = ("Carroll","12.1","13.4","10.4","11.4")
list1= ["Carroll","12.1","13.4","10.4","11.4"]

print(tuple1[0])
print(list1[0])

tuple2 = ("Carroll",)
list2= ["Carroll"]


print(list2[0])
print(tuple2[0])

a = 5
b = 3
print(a,b)
temp = a
a = b
b = temp
print(a,b)

a,b = b,a

print(a,b)

RED = (255,0,0)

