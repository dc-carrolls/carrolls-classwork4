arr1 = [5,12,21,56,102,240]
arr2 = [3,28,42]
arrOut = [0 for _ in range(len(arr1)+len(arr2))]


def merge(arr1,arr2,arrOut):
    p1 = 0
    p2 = 0
    pO = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            arrOut[pO] = arr1[p1]
            p1+=1
            pO+=1
        else:
            arrOut[pO] = arr2[p2]
            p2+=1
            pO+=1
    # By now, either A or B is empty. It remains to empty the other input list.
    while p1 < len(arr1):
            arrOut[pO] = arr1[p1]
            p1+=1
            pO+=1
    while p2 < len(arr2):
            arrOut[pO] = arr2[p2]
            p1+=1
            pO+=1
#end procedure
        


merge(arr1,arr2,arrOut)

print(arrOut)
