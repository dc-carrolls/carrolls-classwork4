import random

def gen_arr1(arr,n)->None:
    arr_seed = [num for num in range(1,n+1)]
    for i in range(n-1):
        arr.append(arr_seed.pop(random.randint(0,n-i-1)))
    #next i
#end procedure

def gen_arr2(arr,n)->None:
    arr_seed = [num for num in range(1,n+1)]
    for i in range(n-2):
        arr.append(arr_seed.pop(random.randint(0,n-i-1)))
    #next i
#end procedure

def find_two_missing_nums(arr,n):
    #mid = 
    pass

def find_one_missing_num(arr,start,end):
    full_series_sum = ((end-start+1)*(start+end))//2
    arr_sum = sum(arr)
    return full_series_sum - arr_sum

my_arr = []

gen_arr1(my_arr,10)

print(my_arr)

print(find_one_missing_num(my_arr,1,10))

my_arr = []

gen_arr2(my_arr,10)

print(my_arr)