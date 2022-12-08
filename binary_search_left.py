def binary_search(A, T):
    L = 0
    R = len(A)-1
    while L < R:
        m = (L + R) // 2
        if A[m] < T:
            L = m + 1
        else:
            R = m
    if A[L] == T:
      return L
    else:
      return - 1

arr = [10,20,30,40,50,60,70,80]

print(binary_search(arr,1))
