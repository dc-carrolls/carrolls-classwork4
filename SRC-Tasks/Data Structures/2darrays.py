# rows, cols = (6, 4)   
# arr = [['X' for i in range(cols)] for j in range(rows)]   
# arr[0][0] = 'O' #assign value at row, column  
# for row in arr:  
#     for x in row:  
#         print(x, end='')  
#     print()  

# my_row = int(input ('Enter column to move to') )
# my_row = my_row - 1						# adjust for rows 1 to 6, not 0 to 5
# my_column = int(input ('Enter column to move to'))
# my_column = my_column - 1				# adjust for columns 1 to 4, not 0 to 3

# arr[0][0] = 'X'
# arr[my_row][my_column] = 'O'
# for row in arr:  
#     for x in row:  
#         print(x, end='')  
#     print()  

RED1 = [255,0,0]
RED2 = (255,0,0)
for i in range(len(RED1)):
    print('RED1',i,RED1[i])
for i in range(len(RED2)):
    print('RED2',i,RED2[i])
RED1[2] = 75
for i in range(len(RED1)):
    print('RED1',i,RED1[i])
RED2 = (255,0,75)
for i in range(len(RED2)):
    print('RED2',i,RED2[i])

