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
    
    # TRSVERSING DFS PREORDER

    def DFS_pre_order(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    # TRAVERSING DFS POSTORDER

    def DFS_post_order(self):
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
        return result
    
    # TRAVERSING DFS INORDER

    def DFS_in_order(self):
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result


myTree=BinarySearchTree()
myTree.insert(47)
myTree.insert(21)
myTree.r_insert(76)
myTree.r_insert(18)
myTree.r_insert(27)
myTree.r_insert(52)
myTree.r_insert(82)
print("Pre-Order -",myTree.DFS_pre_order())  
print("Post-Order -",myTree.DFS_post_order())
print("In-Order :",myTree.DFS_in_order())