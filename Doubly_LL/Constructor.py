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

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
my_list=Doubly_LL(2)
my_list.print_list()
