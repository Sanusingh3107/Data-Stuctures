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

    def heapify(self,index):
        max_ind=index
        while True:
            left_ind=self.left_child(index)
            right_ind=self.right_child(index)

            if left_ind < len(self.heap) and self.heap[left_ind] > self.heap[max_ind]:
                max_ind = left_ind

            if right_ind < len(self.heap) and self.heap[right_ind] > self.heap[max_ind]:
                max_ind = right_ind

            if max_ind != index:
                self.swap(index,max_ind)
                index = max_ind

            else:
                return
            

    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify(0)
        return max_val

my_heap=heap()
my_heap.insert(10)
my_heap.insert(20)
my_heap.insert(15)
my_heap.insert(35)
my_heap.insert(25)
print(my_heap.heap)
my_heap.remove()
print(my_heap.heap)
