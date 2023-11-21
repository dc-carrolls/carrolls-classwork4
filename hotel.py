count = 0
for n in range(1,1000001):
    snum = str(n)
    for c in snum:
        if c == "0":
            count+=1
        #end if
    #next c
#next n
print(count)
