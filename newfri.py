a = [10]




print(a)
a[0]=15
print(a)
while a[0] > 0:
    a[0] = a[0] - 1
    myvalue = a
#endwhile
print(myvalue)
total = 0
for n in range(5):
    total = total + n
#next n
print(total//n)

def mySub():
    global a
    print(a)
    a[0]=54
#end procedure

print('a:',a)
mySub()
print('a:',a)
