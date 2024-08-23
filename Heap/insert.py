class heap:
    def __init__(self):
        self.heap=[]
    
    def left_child(self,index):
        return 2 * index + 1
    
    def right_child(self,index):
        return 2 * index +2

    def parent(self,index):
        return (index - 1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]
    
    def insert(self, val):
        self.heap.append(val)
        cur = len(self.heap) - 1
        while cur > 0 and self.heap[cur] > self.heap[self.parent(cur)]:
            self.swap(cur,self.parent(cur))
            cur=self.parent(cur)

my_heap=heap()
my_heap.insert(10)
my_heap.insert(20)
my_heap.insert(15)
my_heap.insert(35)
my_heap.insert(25)
print(my_heap.heap)
my_heap.insert(40)
print(my_heap.heap)