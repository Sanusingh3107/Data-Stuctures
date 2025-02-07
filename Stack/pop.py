class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    
    def print(self):
        temp=self.top
        while temp:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
    
    def pop(self):
        if self.height==0:
            return None
        self.top=self.top.next
        self.height-=1
s=Stack(5)
s.push(31)
s.push(16)
s.pop()
s.print()