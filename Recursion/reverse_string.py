def reverse(s:str,i:int=-1)->str:
    if i < 0:
        i=len(s)
    if i == 0:
        return ""
    i-=1
    return s[i] + reverse(s,i)
    
print(reverse('hello'))