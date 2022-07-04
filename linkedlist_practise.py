class Node:
    def __init__(self, data=None, next=None):
        self.data = data;
        self.next = next;


class Linkedlist:
    def __init__(self):
        self.head = None;

    def insert_at_beginning(self, data):
            node = Node(data, self.head)
            self.head = node;

    def print(self):
       itr = self.head;
       itrl = []
       while itr:
        itrl.append(itr.data)
        # coma = ' '
        # if itr.next:
        #     coma = ', '
        # itrl += str(itr.data) + coma
        itr = itr.next
       print(itrl)

    def get_length(self):
        count=0;
        itr=self.head;
        while itr:
            count +=1
            itr=itr.next
        return count;


    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None);
            return

        itr = self.head;
        while itr.next:
                itr=itr.next;
        itr.next=Node(data,None)


    def insert_at(self,index,data):
        if index<0 or index >self.get_length():
            raise Exception("invalid index")

        if index==0:
            self.insert_at_beginning(data)
            return

        itr=self.head;
        count = 0;
        while itr:
           if count==index-1:
            node = Node(data,itr.next)
            itr.next=node;
            break
           count +=1;
           itr=itr.next

    def remove_at(self,index):
        
        if index<0 or index > self.get_length():
            raise Exception("invalid index")

        if index==0:
            self.head=self.head.next
            return

        itr=self.head;
        count =0;
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            count +=1;
            itr=itr.next
    def insert_value(self,data):
        itr=self.head;
        for i in data:
            self.insert_at_end(i)


l=Linkedlist()

l.insert_at_beginning(5)
l.insert_at_beginning(15)
l.insert_at_beginning(51)
l.insert_at_beginning(25)
l.insert_at_end(250)
l.insert_at(4,3)
l.print()
l.remove_at(0)
l.print()
l.remove_at(3)
l.print()
l.get_length()

l.insert_value([4,5,6,7,8,91,99])
l.print()
