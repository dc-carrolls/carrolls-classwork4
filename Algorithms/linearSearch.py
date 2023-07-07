gnames = ["Amelia","Olivia","Isla","Emily","Poppy", "Ava","Isabella","Jessica","Lily","Sophie"]
gnums = [1000,3000,4000,3240,5690,9901,2345,3241,3123,4321]
def linear_search(list,item):
    i = 0
    while i < len(list):
        if list[i] == item:
            return i
        #end if
        i = i + 1
    #end while
    return -1
#end function - 10

print(linear_search(gnames,"Lily"))
print(linear_search(gnames,"Amy"))
print(linear_search(gnums,9901))
print(linear_search(gnums,10))


def rec_linear_search(arr,item,index):
    if len(arr) == index:
        return -1
    elif arr[index] == item:
        return index
    else:
        return rec_linear_search(arr,item,index)
    #end if
#end function

print(rec_linear_search(gnums,10,0))