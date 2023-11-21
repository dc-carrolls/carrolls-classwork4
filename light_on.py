# import math as test
# import math_1 as math

# print(math.sqrt(9))
# print(test.sqrt(9))
# def solvr(n,N,light_on):
#     print(n,format(light_on, '08b'))
#     if light_on == (2**N-1):
#         print("solved")
#     elif n == 0:
#         light_on=light_on^1
#         if light_on != 2**N-1:
#             solvr(N-1,N,light_on)
#         else:
#             print("solved")
#         #endif
#     else:
#         light_on=light_on^(2**(n-1))
#         if light_on != 2**N-1:
#             solvr(n-1,N,light_on)
#         else:
#             print("Solved")
#         #endif
#     #endif
# #end procedure

# #solvr(4,4,2)

def bitid(n):
    temp = (n ^ (n >> 1)) ^ ((n+1) ^ ((n+1) >> 1))
    return (temp // temp) & -temp

print(bitid(5))

