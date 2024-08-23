class Node:
    def  __init__(self,value):
        self.value=value
        self.next=None 

class LinkedList:
    def __init__(self,value):
        new_node =Node(value)
        self.head=new_node
        self.tail=new_node
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def print(self):
        node=self.head
        while True :
            print (node.value , end=" ")
            if node==self.tail:
                break
            node=node.next

L=LinkedList(4)
L.append(3)
L.append(2)
L.print() # Outputs: 4 3 2