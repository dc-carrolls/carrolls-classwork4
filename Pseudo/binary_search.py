def binarySearch(arr, item):
    lower = 0
    upper = len(arr) - 1
    while not(upper - lower < 0): #BRP
        mid = (lower + upper) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            lower = mid + 1
        else:
            upper = upper - 1
        #end if
    #end while
    return -1
#end function

my_list = [10,13,18,18,56,109,209,420]

print(binarySearch(my_list, 18))


# def binarySearchL(arr, item):
#     lower = 0
#     upper = len(arr) - 1
#     while lower < upper:
#         mid = (lower + upper) // 2
#         if arr[mid] < item:
#             lower = mid + 1
#         else:
#             upper = mid
#     return lower


# print(binarySearchL(my_list,18))