class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value
  
 
def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.val == value:
            return root
        elif root.val < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root
 
# A utility function to search a given value in BST
def search(root,value):
     
    # Base Cases: root is null or value is present at root
    if root is None or root.val == value:
        return root
 
    # value is greater than root's value
    if root.val < value:
        return search(root.right,value)
   
    # value is smaller than root's value
    return search(root.left,value)
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
# Create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)


    
