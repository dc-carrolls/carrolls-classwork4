# importing numpy module
import numpy as np
 
# creating list
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
 
# creating numpy array
sample_array = np.array([list_1,
                         list_2,
                         list_3])
 
print("Numpy multi dimensional array in python\n",
      sample_array)

# print shape of the array
print("Shape of the array :",
      sample_array.shape)

test=np.empty([4, 3],
         dtype = 10U)

print(test)

number_text = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven']

for n in range(12):
    test[n//3,n%3]=number_text[n]

print(test)
