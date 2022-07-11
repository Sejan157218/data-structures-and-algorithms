import re


class BinarySearchTreenode():
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;

    def add_child(self,data):
        if self.data==data:
            return "data already exists";

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTreenode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreenode(data)


    def Search(self, val):
        if self.data == val:
            return True;

        if val < self.data:
            if self.left:
                return self.left.Search(val);
            else:
                return False
        if val > self.data:
             if self.left:
                return self.left.Search(val);
             else:
                return False


    def in_order_traversal(self):
        elements=[];
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements;
    def pre_order_traversal(self):
        elements=[];
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements;
    def post_order_traversal(self):
        elements=[];
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements;

    def find_max(self):
        if self.right is None:
            return self.data;
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data;
        return self.left.find_min()

    def calculate_sum(self):
        left_side= self.left.calculate_sum() if self.left else 0
        right_side= self.right.calculate_sum() if self.right else 0

        return left_side + right_side + self.data


    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        if val > self.data:
            if self.right:
                self.right.delete(val)
        
        else:
            if self.left is None and self.right is None:
                return None;
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left;
            min_val=self.right.find_min()
            self.data=min_val;
            self.right = self.right.delete(min_val)

        return self



def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreenode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root;


if __name__ == "__main__":
    # root = BinarySearchTreenode(10)
    # root.add_child(7)
    # root.add_child(12)
    # root.add_child(6)
    # root.add_child(16)
    # print(root.in_order_traversal())
    # print(root.in_order_traversal())
    # print(root.pre_order_traversal())
    # print(root.post_order_traversal())

    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)
    # print("post order traversal gives this sorted list:",country_tree.post_order_traversal())
    # print("UK is in the list? ", country_tree.Search("UK"))
    # print("Sweden is in the list? ", country_tree.Search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

    # print("Min:",numbers_tree.find_min())
    # print("Max:",numbers_tree.find_max())

    # print("Sum:", numbers_tree.calculate_sum())
    numbers_tree.delete(20)
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
