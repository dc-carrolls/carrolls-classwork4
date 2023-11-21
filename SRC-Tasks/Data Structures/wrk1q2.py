MAX = 12
name_array = ["" for _ in range(MAX)] #Array creation

name_array[0] = "Bob"
name_array[1] = "Fred"
name_array[2] = "Barry"
name_array[3] = "Felix"

search_name = input("Enter Name to Find:")
index = 0
found = False
while not found and index < MAX:
    if name_array[index] == search_name:
        found = True
    #end if 
    index = index + 1
#end while
if found:
    print(index)
else:
    print("not found!")
#end if


print(name_array)