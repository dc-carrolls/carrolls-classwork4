x = ord("a")
print(x)
x = x ^ 0x20
print(x)
print(chr(x))
x = x ^ 32
print(chr(x))

cnum = "9"
anum = ord(cnum)
num = anum & 0b00001111
print(num * 5)

