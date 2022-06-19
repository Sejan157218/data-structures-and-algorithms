# class HashTable:
#     def __init__(self):
#         self.Max=100;
#         self.arr = [None]*self.Max;

#     def get_hashKey(self,key):
#         sum=0;
#         for c in key:
#             sum +=ord(c)
#         return sum % self.Max

#     def __setitem__(self,key,value):
#         h=self.get_hashKey(key);
#         self.arr[h]=value;
#         return self.arr;

#     def __getitem__(self,key):
#         h=self.get_hashKey(key);
#         return self.arr[h];


# if __name__ == '__main__':
#     h = HashTable()
#     print(h.get_hashKey("haseeh"))
#     print(h.__setitem__("haseeh",303))
#     print(h.__getitem__("haseeh"))




# Collision handling with link list
class HashTable:
    def __init__(self):
        self.Max=10;
        self.arr=[[] for i in range(self.Max)];


    def get_hash(self,key):
        hash=0;
        for i in key:
            hash +=ord(i);
        return hash % self.Max;


    def get_item(self,key):
        h=self.get_hash(key);
        for kv in self.arr[h]:
            if kv[0]==key:
                return kv[1];
    
    def __setItem__(self,key,value):
        h=self.get_hash(key);
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[idx]==key:
                self.arr[h][idx]=(key,value);
                found=True
        if not found:
            self.arr[h].append((key,value));

    def del_item(self,key):
        h=self.get_hash(key);
        for idx,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][idx]



if __name__ == '__main__':
    h = HashTable()
    print(h.get_hash("haseeh"))
    print(h.__setItem__("march 6",303))
    print(h.__setItem__("march 17",305))
    print(h.get_item("march 17"))
    print(h.del_item("march 17"))
    print(h.arr)