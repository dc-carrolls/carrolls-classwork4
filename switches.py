# def switch_press(n,N,light_on):
#   print("Switch",n,"of",bin(light_on))
#   if light_on == 15:
#     return
#   elif n == N:
#     # press 1
#     switch_press(N-1,N,light_on^(2**(N-1)))
#   else:
#     switch_press(n-1,N,light_on^(2**(n-1)))


def switch_press(n,N,light_on):
  print("Switch",n,"of",bin(light_on))
  if light_on == (2**N)-1:
    print("light on")
    return
  if n == 0:
    light_on = light_on^1
    if light_on != (2**N)-1:
      switch_press(N-2,N,light_on^2**(N-1))
  elif n > 0:
    switch_press(n-1,N,light_on^(2**(n)))
  


#switch_press(1,3,1)

def next_gray(n):
  return n ^ (n>>1)

print(next_gray(9))



  