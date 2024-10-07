myList = [1,4,13,27,32,37,56,83,102,115] 

def linearSearchFor(arr,item):
    retIndex = -1
    for index in range(len(arr)):
        if arr[index] == item:
            retIndex = index
        #end if
    #next index
    return retIndex
#end function

def linearSearchWhile(arr, item):
    index = 0
    while index < len(arr) and item != arr[index]:
        index = index + 1
    #end while
    if index == len(arr):
        return -1
    else:
        return index
    #end if
#end function




print(linearSearchWhile(myList,83))

