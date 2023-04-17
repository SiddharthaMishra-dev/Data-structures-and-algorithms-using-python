class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
def height(root):
    if root is None:
        return 0
    else:
        leftheight=height(root.left)
        rightheight=height(root.right)
        return (max(leftheight,rightheight)+1)


root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(height(root))