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

    def pop(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            pre =self.head
            while(temp.next):
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
    
    def print(self):
        node=self.head
        while True :
            print ('\n',node.value , end=" ")
            if node==self.tail:
                break
            node=node.next

L=LinkedList(4)
L.append(3)
L.append(2)
L.print() # Outputs: 4 3 2
L.pop()
L.print() # Outputs: 4 3