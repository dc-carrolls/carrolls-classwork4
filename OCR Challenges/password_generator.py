import random

def gen_pwd(len :int)->str:
    pwd_chars = [n for n in range(33,127)]
    nums = pwd_chars[15:25]
    ucase = pwd_chars[32:58]
    lcase = pwd_chars[64:90]
    symbl = [n for n in pwd_chars if n not in nums + ucase + lcase]
    pwd = []
    pwd.append(chr(random.choice(nums))) # Number
    pwd.insert(random.randint(0,1),chr(random.choice(ucase))) # Upper Case
    pwd.insert(random.randint(0,2),chr(random.choice(lcase))) # Lower Case
    pwd.insert(random.randint(0,3),chr(random.choice(symbl))) # Symbol
    for i in range(4,len):
        pwd.insert(random.randint(0,i),chr(random.choice(pwd_chars)))
    # next i
    return ''.join(pwd)
# end function

print(gen_pwd(15))


