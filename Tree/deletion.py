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
    
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    def delete_node(self,value):
        self._delete_node(self.root,value)

    def _delete_node(self,current_node,value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self._delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node=current_node.right
            elif current_node.right is None:
                current_node=current_node.left
            else:
                min_node = self.min_value(current_node.right)
                current_node.value = min_node
                current_node.right = self._delete_node(current_node.right,value)
        return current_node



myTree=BinarySearchTree()
myTree.insert(2)
myTree.insert(1)
myTree.r_insert(3)
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
myTree.delete_node(3)
print("After Deletion")
print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right)