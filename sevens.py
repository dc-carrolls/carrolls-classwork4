def count7s(num):
    digits = [int(z) for z in num[::-1]+'9']
    #digits = num[::-1]+'0'
    print(digits)
    total = 0
    mult = len(digits) - 2
    for i in range(mult): 
        if digits[i] >= 7:
            total = total + (digits[i+1]+1)*10**(mult-1) 
        elif digits[i] < 7:
            total = total + digits[i+1] * 10**(mult-1)
        #end if
        print(total)
    #next i
    print(total)

def count7s2(digits):
    total = 0
    num = int(digits)
    for n in range(1,num+1):
        for c in str(n):
            if c == '7':
                total+=1
            #end if
        #next c
    #next n
    print(total)

def countfirstcol(digits):
    n = len(digits) - 1
    digit = int(digits[0])
    if digit > 7:
        return 10**n
    elif digit < 7:
        return 0
    else:
        return int(digits[1:])+1
    
def countnextcol(digits,col):
    n = len(digits)-1
    digit = int(digits[col])
    if digit > 7:
        return di

                
            



#count7s('86')
print(countfirstcol('7'))



