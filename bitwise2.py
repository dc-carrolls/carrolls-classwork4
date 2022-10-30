party = [6,2,4,5,6,2,4]
answer = 0
for n in party:
    answer = answer ^ n
print(answer)

count = {}
for n in party:
    if n in count:
        count[n]+=1
    else:
        count[n]=1
for key in count:
    if count[key] == 1:
        print(key)


tuple_of_tuples = ((0,0),(0,1),(1,1))
print(tuple_of_tuples[1][1])
tuple_of_lists = ([0,0],[0,1],[1,1])
print(tuple_of_lists)
tuple_of_lists[0][0]=2
print(tuple_of_lists)
  