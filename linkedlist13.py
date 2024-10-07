class Node:
    def __init__(self,name,pointer) -> None:
        self.name = name
        self.pointer = pointer
    #end constructor
    def __str__(self) -> str:
        return "\033[1mData:"+self.name+",Ptr:"+str(self.pointer)+"\033[0m"
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

