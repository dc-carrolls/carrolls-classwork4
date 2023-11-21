data = ["B","A","C","F","E","D"]


def worst_bubble(arr):
    for j in range(1,len(arr)): # for j = 1 to len(arr)-1
        for i in range(len(arr)-1): # for i=0 to len(arr)-2
            if arr[i] > arr[i+1]:
                #swap
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            #end if
        #next i
    #next j
#end procedure



def second_worst_bubble(arr):
    for j in range(1,len(arr)): # for j = 1 to len(arr)-1
        for i in range(len(arr)-j): # for i=0 to len(arr)-2
            if arr[i] > arr[i+1]:
                #swap
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            #end if
        #next i
    #next j
#end procedure


def best_bubble(arr):
    sorted = False
    j=1
    while not sorted and j < len(arr):
        sorted = True
        for i in range(len(arr)-j): # for i=0 to len(arr)-2
            if arr[i] > arr[i+1]:
                #swap
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                sorted = False
            #end if
        #next i
        j += 1
    #end while
#end procedure

print(data)
best_bubble(data)
print(data)
