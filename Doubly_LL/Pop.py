class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev=None
class Doubly_LL:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp.value
        
my_list=Doubly_LL(2)
my_list.append(3)
my_list.append(33)
print(my_list.pop())
print(my_list.pop())
print(my_list.pop())
# my_list.print_list()
