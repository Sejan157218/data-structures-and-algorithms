class Treenode():
    def __init__(self,name,designation):
        self.name=name;
        self.designation=designation;
        self.children=[];
        self.parent=None;


    def add_child(self,child):
        child.parent=self;
        self.children.append(child)

    
    def Get_level(self):
        level=0;
        p=self.parent;
        while p:
            level +=1;
            p=p.parent
        return level;


    def print_tree(self,property_name):


        if property_name=="name":
            value= self.name;
        if property_name == "designation":
            value=self.designation;
        
        if property_name == "both":
            value=self.name +" ("+ (self.designation) + ")";

        spaces = " " * self.Get_level() * 4
        prefix=spaces + "!--"
        print(prefix + value);
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def build_management_tree():
    ceo=Treenode("Sejan","CEO")
    cto=Treenode("sajal","CTO")
    Infrastructure_head=Treenode("sajal1","infrastructure-Head")
    Infrastructure_head.add_child(Treenode("sejan1","Cloud Manager"))
    Infrastructure_head.add_child(Treenode("sejan2","App Manager"))

    Hr_head=Treenode("sajal2" ,"HR-Head")
    Hr_head.add_child(Treenode("sejan3","Recruitment-Head"))
    Hr_head.add_child(Treenode("sejan4","policy_Manager"))

    ceo.add_child(cto)
    ceo.add_child(Hr_head)

    cto.add_child(Infrastructure_head)
    cto.add_child(Hr_head)
    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")
