print("Please enter values for a, b and c")
a,b,c = [int(x) for x in input().split()]

x = a * b + c
y = (b + c) / a
z = x // y	
w = x % y 
#x = x + y
print(x)	
print(y)	
print(z)	
print(w)	


