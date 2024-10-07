numbers = [3, 6, 2, 8, 1]

def iterTotal(arr)->int:
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    #next i
    return total
#end function

print(iterTotal(numbers))

def recurTotal(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recurTotal(arr[1:])
    #end if
#end function

print(recurTotal(numbers))


def addOne(n):
	if n < 4:
		print (n)
		addOne(n + 1)
	else:
		print (n)
	#endif
#endprocedure
addOne(1) 

def sumEven(n:int)->int:
    total = 0
    for i in range(2,n+1,2):
        total = total + i
    #next i
    return total
#end function

def rSumEven(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + rSumEven(n-2)
    #end if
#end function

print(rSumEven(10))
    
    
                  
            
