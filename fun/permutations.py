def gen_next_perm(digits:list)->bool:
    # Step 1: Find the largest k such that digits[k] < digits[k+1]
    k = -1
    last_idx = len(digits)-1
    for i in range(last_idx):
        if digits[i] < digits[i + 1]:
            k = i
        #end if
    # next i

    # If no more permutations available exit with False
    if k == -1:
        return False
    # end if

    # Step 2: Find the largest l greater than k such that digits[k] < digits[l]
    l=last_idx
    while digits[k] >= digits[l]:
      l-=1
    # end while

    # Step 3: Swap digits[k] and digits[l]
    temp = digits[k]
    digits[k] = digits[l]
    digits[l] = temp

    # Step 4: Reverse the sequence from digits[k+1] to the end
    digits[k + 1:] = digits[:k:-1]

    return True
# end function

def gen_all_perms(digits:list)->None:
    
    # Print the first permutation
    print(digits)
    
    # Keep generating and printing the next permutation until there are no more
    while gen_next_perm(digits):
        print(digits)
    # end while
# end procedure

# Example usage
# digits = ['a', 'b', 'c', 'd']
# digits = [1, 2, 3, 4]
digits = [4, 4, 8, 8]
gen_all_perms(digits)


# def reverse_section(arr):
#     print(arr[2:]) 
#     print(arr[:1:-1])
#     arr[2:] = arr[:1:-1]



# reverse_section(digits)
# print(digits)
