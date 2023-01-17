arr = [4, 6, 1, 5, 7, 8]

def bubble1(arr):
    flag = True
    i = 0
    while flag:
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
                flag = True
            #end if

        #next j
        i = i + 1
        print(arr)
    #next i
#end procedure

def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp 


bubble1(arr)
print(arr)

