arr = [9,5,4,15,3,8,11]

def insertion_sort(nums):
    for pos in range(1,len(nums)):
        currentItem = nums[pos]
        while pos > 0 and nums[pos -1]> currentItem:
            nums[pos] = nums[pos -1]
            pos = pos -1
        #end while
        nums[pos]=currentItem
    #next pos
#end procedure

print(arr)
insertion_sort(arr)
print(arr)

