class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor

    def __repr__(self) -> str:
        return "Data:"+self.name+",Ptr:"+str(self.pointer)
#end Node record

# Create array of blank Nodes (records)
myList = [Node("",-1) for _ in range(5) ]

for index in range(4):
    myList[index].pointer = index + 1
#next index
myList[4].pointer = -1


start = -1
nextfree = 0

print(myList)

def outputList(arr):
    global start
    current_pointer = start
    while current_pointer != -1:
        print(arr[current_pointer].name)
        current_pointer=arr[current_pointer].pointer
    #end while
#end procedure

def AddItem(newItem, myList):
    global start
    global nextfree
    # check if list is full and if so, print error message
    if nextfree == -1:
        print("List is Full")
    else: 
        myList[nextfree].name = newItem
        if start == -1:
            temp = myList[nextfree].pointer     #save pointer
            myList[nextfree].pointer = -1
            start = nextfree
            nextfree = temp
        else:
            p = start
            if newItem < myList[p].name:
                myList[nextfree].pointer = start
                start = nextfree
            else:    
                placeFound = False	#general case
                while myList[p].pointer != -1 and placeFound == False:
                # peek ahead
                    if newItem >= myList[myList[p].pointer].name:
                        p = myList[p].pointer
                    else:
                        placefound = True
					#endif
				#endwhile
                temp = nextfree
                nextfree = myList[nextfree].pointer
                myList[temp].pointer = myList[p].pointer
                myList[p].pointer = temp
			#endif
		#endif
	#endif
#endprocedure




AddItem("Colin",myList)
AddItem("Albert",myList)
# AddItem("Barry",myList)
# AddItem("Derek",myList)
# AddItem("Fred",myList)
outputList(myList)
# AddItem("Trevor",myList)





# def AddItem(newItem, myList):
#     global start
#     global nextfree
#     # check if list is full and if so, print error message
#     if nextfree == -1:
#         print("List is Full")
#     else: 
#         myList[nextfree].name = newItem
#         if start == -1:
#             temp = myList[nextfree].pointer     #save pointer
#             myList[nextfree].pointer = -1
#             start = nextfree
#             nextfree = temp
#         else:
#             p = start
#             if newItem < myList[p].name:
#                 myList[nextfree].pointer = start
#                 start = nextfree
#             else:    
#                 placeFound = False	#general case
#                 while myList[p].pointer != -1 and placeFound == False:
#                 # peek ahead
#                     if newItem >= myList[myList[p].pointer].name:
#                         p = myList[p].pointer
#                     else:
#                         placefound = True
# 					#endif
# 				#endwhile
#                 temp = nextfree
#                 nextfree = myList[nextfree].pointer
#                 myList[temp].pointer = myList[p].pointer
#                 myList[p].pointer = temp
# 			#endif
# 		#endif
# 	#endif
# #endprocedure


