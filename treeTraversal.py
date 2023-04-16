class Node:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def inorderTraversal(root):
    if root is None:
        return []
    return (inorderTraversal(root.left)+ [root.val] + inorderTraversal(root.right))


def preorderTraversal(root):
    if root is None:
        return []
    return ([root.val] + preorderTraversal(root.left) + preorderTraversal(root.right))


def postorderTraversal(root):
    if root is None:
        return []
    return (postorderTraversal(root.left)+ postorderTraversal(root.right)+ [root.val])


root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(inorderTraversal(root))
print(preorderTraversal(root))
print(postorderTraversal(root))