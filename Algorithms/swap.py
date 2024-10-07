arr = [7,4,6,8,1,5]
names = ['Sophie', 'Lily', 'Jessica', 'Isabella', 'Ava', 'Poppy', 'Emily', 'Isla', 'Olivia', 'Amelia']
def swap(a,b,arr):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp
#end procedure
    
def swap2(a,b,arr):
    arr[b],arr[a] = arr[a],arr[b]

#end procedure
    
first,*middle,last = "Hello"   
print(first, middle, last)

print(arr)
swap2(0,1,arr)
print(arr)


def bubble_sort(arr):
    for i in range(len(arr)-1): # for i = 0 to n - 2
        for j in range(len(arr) - 1 - i): # for j = 0 to n - i - 2
            if arr[j] > arr[j+1]:
                swap(j,j+1,arr)
            #end if
        #next j
    #next i
#end procedure
print(names)              
bubble_sort(names)
print(names)