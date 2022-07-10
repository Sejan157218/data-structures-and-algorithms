class Treenode():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() *3
        prefix="!--" if self.parent else ""
        print(spaces + prefix + self.data)

        for child in self.children:
            child.print_tree()


def build_product_tree():

    root = Treenode("Electronics")

    laptop = Treenode("laptop")
    laptop.add_child(Treenode("Mac"))
    laptop.add_child(Treenode("Thinkpad"))

    tv = Treenode("tv")
    tv.add_child(Treenode("Sony"));
    tv.add_child(Treenode("Rangs"));
    tv.add_child(Treenode("Walton"));


    cellphone=Treenode('cellphone');
    cellphone.add_child(Treenode("Redmi"));
    cellphone.add_child(Treenode("Realmi"))

    root.add_child(laptop)
    root.add_child(tv)
    root.add_child(cellphone)


    root.print_tree()


    # root.add_child(tv)


build_product_tree()
