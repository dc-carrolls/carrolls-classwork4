class BSTree:
    def __init__(self, root) -> None:
        self._root = root
        
    def root(self):
        return self._root

class Node:
    def __init__(self, breed):
        self._breed = breed
        self._left = None
        self._right = None
    #end constructor

    def __repr__(self) -> str:
        msg = 'Node:' + self._breed
        if self._left == None:
            msg = msg + '\nLeft:None'
        else:
            msg = msg + '\nLeft:' + self._left._breed
        if self._right == None:
            msg = msg + '\nRight:None'
        else:
            msg = msg + '\nRight:' + self._right._breed
        return msg

    def getBreed(self):
        return self._breed

    def getLeftNode(self):
        return self._left

    def setLeftNode(self,left):
        self._left = left

    def getRightNode(self):
        return self._right

    def setRightNode(self,right):
        self._right = right


def insert(root, value):
    newnode = Node(value)
    cn = root # Current Node (cn) set to root
    while (cn != None):
        pn = cn # Set previous node equal to current node
        if (value < cn.getBreed()):
            cn = cn.getLeftNode()
        else:
            cn = cn.getRightNode()
        #end if
    #end while
    if (value < pn.getBreed()):
        pn.setLeftNode(newnode)
    else:
        pn.setRightNode(newnode) 
    # end if
#end procedure

def traverseBST(root,order=2): # order=1 for pre-order, 2 for in-order 3 for post-order
    if order == 1: print(root.getBreed(), end=" ")
    if (root.getLeftNode() != None):
        traverseBST(root.getLeftNode())
    if order == 2: print(root.getBreed(), end=" ")
    if (root.getRightNode() != None):
        traverseBST(root.getRightNode())
    if order == 3: print(root.getBreed(), end=" ")

def main():
    breeds = ['Harrier','Greyhound','Rottweiler','Chihuaha','Pug','Whippet','Doberman','Dalmatian']
    tree = BSTree(Node(breeds[0])) # Create tree with root node
    for breed in breeds[1:]:
        insert(tree.root(),breed) # Insert rest of nodes into tree
    traverseBST(tree.root()) # Output Tree (in-order)
    print("\nStart...")
    name = input("Enter the name of a breed:")
    breedNode = tree.root()
    found = False
    while breedNode != None and not found:
        if breedNode.getBreed() == name:
            found = True
        elif name < breedNode.getBreed():
            breedNode = breedNode.getLeftNode()
        else:
            breedNode = breedNode.getRightNode()
        #end if
    #end while
    if breedNode == None:
        print(name, 'is not in the tree.')
    else:
        print(name, 'is in the tree.')
    #end if
   

if __name__ == '__main__':
    main()


