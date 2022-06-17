# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class linkedlist:
#     def __init__(self):
#         self.head = None

#     def insert_at_beginning(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def print(self):
#         head_index = self.head
#         list = ''
#         while head_index:
#             split_icon = ''
#             if head_index.next:
#                 split_icon = ',';
#             list += str(head_index.data) + split_icon;
#             head_index = head_index.next
#         print(list)

#     def insert_at_end(self,data):
#         # if self.head is None:
#         #     self.head=Node(data,None)
#         #     return
#         # head_index=self.head;
#         # while head_index.next:
#         #     head_index = head_index.next;
#         # head_index.next=Node(data)
#         if self.head is None:
#             self.head=Node(data,None);
#             return
#         itr = self.head
#         while itr.next:
#             itr= itr.next;
#         itr.next= Node(data)

#     def insert_values(self,data):
#         self.head=None
#         for i in data:
#             self.insert_at_end(i);
    
#     def insert_after_value(self,pre_value,after_value):
#         if self.head is None:
#             return 

#         if self.head.data==pre_value:
#             self.head.next=Node(after_value,self.head.next)
#             return

#         itr=self.head
#         while itr:
#             if itr.data==pre_value:
#                 itr.next=Node(after_value,itr.next)
#                 break
#             itr=itr.next

#     def remove_by_value(self,remove_value):
#         if self.head is None:
#             return
        
#         if self.head == remove_value:
#             self.head == self.head.next
#             return
#         itr = self.head;
#         while itr.next:
#             if itr.next.data == remove_value:
#                 itr.next=itr.next.next
#                 break
#             itr=itr.next



# if __name__ == '__main__':
#     # data = linkedlist()
#     # data.insert_at_beginning(5)
#     # data.insert_at_beginning(4)
#     # data.insert_at_beginning(6)

#     # data.print()

#     # data.insert_at_end(10)
#     # data.insert_at_end(20)
#     # data.insert_at_end(30)
#     # data.print()
#     ll = linkedlist()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple") 
#     ll.print()
#     ll.remove_by_value("apple")
#     ll.remove_by_value("orange")
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        head_index = self.head
        list = ''
        while head_index:
            split_icon = ''
            if head_index.next:
                split_icon = ',';
            list += str(head_index.data) + split_icon;
            head_index = head_index.next
        print(list)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None);
            return
        itr = self.head
        while itr.next:
            itr= itr.next;
        itr.next= Node(data)



if __name__ == '__main__':
    data = linkedlist()
    data.insert_at_beginning(5)
    data.insert_at_beginning(4)
    data.insert_at_beginning(6)
    data.print()
