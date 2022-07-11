class TreeNode():
    def __init__(self,data):
        self.data=data;
        self.children=[];
        self.parent=None;

    
    def add_child(self,child):
        child.parent = self;
        self.children.append(child);

    def get_level(self):
        level=0;
        p=self.parent;
        while p:
            level +=1;
            p=p.parent;
        return level;


    def print_tree(self,level):
    
        spaces=" " * self.get_level() * 4;
        prefix=spaces + "!--" if self.parent  else " " 
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

        
def build_location_tree():
    global_location = TreeNode("GLobal");

    bangladesh=TreeNode("Bangladesh");
    usa=TreeNode("USA");

    dhaka=TreeNode("Dhaka")
    dhaka.add_child(TreeNode("Dhaka-North"))
    dhaka.add_child(TreeNode("Dhaka-South"))

    mymenshing=TreeNode("Mymenshing")
    mymenshing.add_child(TreeNode("mymenshing-North"))
    mymenshing.add_child(TreeNode("mymenshing-South"))
 

    new_jersey=TreeNode("New-Jersey")
    new_jersey.add_child(TreeNode("New-Jersey-North"))
    new_jersey.add_child(TreeNode("New-Jersey-South"))

    california=TreeNode("California")
    california.add_child(TreeNode("California-North"))
    california.add_child(TreeNode("California-South"))

    global_location.add_child(bangladesh)
    global_location.add_child(usa)

    bangladesh.add_child(dhaka)
    bangladesh.add_child(mymenshing)

    usa.add_child(new_jersey)
    usa.add_child(california)
    return global_location;


if __name__ == '__main__':
    root_node=build_location_tree()
    root_node.print_tree(1)
        