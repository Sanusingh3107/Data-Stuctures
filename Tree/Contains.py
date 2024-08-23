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
                    
    def Contains(self,value):
        if self.root==None:
            return False
        temp=self.root
        while temp:
            if value==temp.value:
                return True
            elif value<temp.value:
                temp=temp.left
            elif value>temp.value:
                temp=temp.right
            else:
                return False
            
# Recursive Contains
            
    def r_contain(self,value):
        return self._r_contains(self.root,value)
    
    def _r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._r_contains(current_node.left, value)
        elif value > current_node.value:
            return self._r_contains(current_node.right, value)
            
            


myTree=BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
print(myTree.Contains(3))

# Recursive Contains

print(myTree.r_contain(1))
print(myTree.r_contain(4))