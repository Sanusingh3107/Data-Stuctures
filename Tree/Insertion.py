class Node:
    def __init__(self,value):
        self.value = value
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        new_node=Node(value)
        if self.root==None:
            self.root=new_node
            return True
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            elif new_node.value<temp.value:
                if temp.left==None:
                    temp.left=new_node
                    return True
                else:
                    temp=temp.left
            else:
                if temp.right==None:
                    temp.right=new_node
                    return True
                else:
                    temp=temp.right

# Recursion Insertion

    def _r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self._r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self._r_insert(current_node.right, value)
        return current_node


    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        return self._r_insert(self.root,value)



myTree=BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.r_insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)