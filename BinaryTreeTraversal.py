#Thsi Program traverses the Binary Tree in 3 Ways: In/Post/Pre-Order
class Node:
    def  __init__ (self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right, key)
        else:
            root.left=insert(root.left, key)
    return root


def preorder(root):
     if root:                           #You can change the sequence accordingly for inorder and postorder
         print(root.val)
         preorder(root.left)
         preorder(root.right)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
print("Pre-Order Traversal: ") 
preorder(r)
print("In-Order Traversal: ")
inorder(r)
print("Post-Oder Traversal: ")
postorder(r)