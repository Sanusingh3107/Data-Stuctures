class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size
    
    def _hash(self,key):
        my_hash=0
        for letter in key:
            my_hash=(my_hash + ord(letter) *23) % len(self.data_map)
        return my_hash
    
    def set_item(self,key,value):
        index=self._hash(key)
        if self.data_map[index]==None:
            self.data_map[index]=[]
        self.data_map[index].append([key,value])

    def get_items(self,key):
        index=self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
    
    def print_table(self):
        for index, value in enumerate(self.data_map):
            print(f"{index}: {value}")

hst=HashTable()

hst.set_item('grapes',13)
hst.set_item('apples',7)
hst.set_item('bananas',3)

print(hst.get_items('apples'))
