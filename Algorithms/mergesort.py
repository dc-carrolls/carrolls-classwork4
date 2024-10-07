def merge(new_list,lefthalf,righthalf):
    left_idx = 0
    right_idx = 0
    new_idx = 0
    while left_idx < len(lefthalf) and right_idx < len(righthalf):
        if lefthalf[left_idx] < righthalf[right_idx]:
            new_list[new_idx] = lefthalf[left_idx]
            left_idx = left_idx + 1
        else:
            new_list[new_idx] = righthalf[right_idx]
            right_idx = right_idx + 1
        #endif
        new_idx = new_idx + 1
    #endwhile
#check if the left half still has elements not merged 
#if so, add them to alist 
    while left_idx < len(lefthalf):
        new_list[new_idx] = lefthalf[left_idx]
        left_idx = left_idx + 1
        new_idx = new_idx + 1
    #endwhile
#check if the right half still has elements not merged 
#if so, add them to alist 
    while right_idx < len(righthalf):
        new_list[new_idx] = righthalf[right_idx]
        right_idx = right_idx + 1
        new_idx = new_idx + 1
    #endwhile
#endprocedure


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2    	# performs integer division
        lefthalf = alist[:mid]    	# left half of alist put into lefthalf
        righthalf = alist[mid:]   	# right half of alist put into righthalf
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
			#endif
            k = k + 1
		#endwhile
#check if the left half still has elements not merged 
#if so, add them to alist 
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
		#endwhile
#check if the right half still has elements not merged 
#if so, add them to alist 
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
		#endwhile
        print("Merged sublist ",alist)
	#endif        
#endprocedure

def mergeSort2(alist):
    if len(alist) > 1:
        mid = len(alist) // 2    	# performs integer division
        lefthalf = alist[:mid]    	# left half of alist put into lefthalf
        righthalf = alist[mid:]   	# right half of alist put into righthalf
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(alist,lefthalf,righthalf)
        print("Merged sublist ",alist)
	#endif        
#endprocedure


#*********** MAIN PROGRAM ***************
alist = [3, 1, 9, 8, 4, 6]
print("Unsorted list: ",alist)
mergeSort2(alist)
print("Sorted list: ",alist)

# blist = [2,5,12,14,17]
# clist = [0 for _ in range(len(alist)+len(blist))]


# print(blist)       
# merge(clist,alist,blist)
# print(clist)
        

        
    

