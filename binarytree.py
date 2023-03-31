class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,value):
        if self.data:
            if self.data<value:
                if self.right is None:
                    self.right=Node(value)
                else:
                    self.right.insert(value)
            elif self.data>value:
                if self.left is None:
                    self.left=Node(value)
                else:
                    self.left.insert(value)
        else:
            self.data=value
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

root=Node(12)
root.insert(2)
root.insert(10)
root.insert(15)
root.insert(9)
root.printTree()
