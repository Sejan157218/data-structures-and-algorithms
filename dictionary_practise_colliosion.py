class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range (self.Max)]


    def hash_key(self,key):
        sum=0;
        for c in key:
            sum += ord(c);
        return sum % self.Max;
    
    def get_item(self,key):
        h= self.hash_key(key)
        for kv in self.arr[h]:
            if kv[0]==key:
                return kv[1];

    def set_item(self,key,value):
        h=self.hash_key(key)
        found=False
        for inx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[inx]==key:
                self.arr[h][inx]=(key,value);
                found=True
        if not found:
            self.arr[h].append((key,value))

    def del_item(self,key):
        h=self.hash_key(key)
        for inx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][inx];
      

               
             


h=HashTable()
h.set_item('sejan',2)
h.set_item('seajn',5)
h.set_item('sean',5)
h.set_item('sajn',5)
print(h.get_item('seajn'))
h.del_item('sajn')
print(h.arr)



