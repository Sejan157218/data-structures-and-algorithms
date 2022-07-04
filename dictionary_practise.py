class HashTable():
    def __init__(self) :
        self.Max=100;
        self.arr=[None] * self.Max;

    def hash_key(self,key):
        sum=0;
        for c in key:
            sum +=ord(c)
        return  sum %  self.Max


    def __setItem__(self,key,value):
        h=self.hash_key(key)
        self.arr[h]=value
        print(self.arr)

    def __getItem__(self,key):
        h=self.hash_key(key)
        value=self.arr[h]   
        return value

    def deleteItem(self,key):
        h=self.hash_key(key)
        self.arr[h]=None

h=HashTable()
h.__setItem__('sejan',11111111111111)
print(h.__getItem__('sejan'))
h.deleteItem('sejan')
print(h.__getItem__('sejan'))
