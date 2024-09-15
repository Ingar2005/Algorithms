class Bin_tree:

    def __init__(self):
        self.root = -1
    def add_node(self,node):

        current = self.root
        while True:
            if self.root ==-1:
                self.root = node
                break
            if  (current.data>node.data):
                if current.left == None:
                    current.add_left(node)
                    break
                else: current = current.left

            if (current.data <=node.data):
                if current.right == None :
                    current.add_right(node)
                    break
                else: current = current.right




    def repr(self):
        try:
            self.root.in_order()
        except:
            print("sorry nothing here")

class Node:

    def __init__(self,data:int):
        self.data = data
        self.left = None
        self.right = None
    def add_left(self,node):
        self.left = node
    def add_right(self,node):
        self.right = node

    def in_order(self):
        if self.left != None:
            self.left.in_order()
        print(self.data, end=' ')
        if self.right != None:
            self.right.in_order()

if __name__=="__main__":
    tree = Bin_tree()
    nodes = [Node(5),Node(3),Node(8),Node(1),Node(8),Node(4)]
    for i in nodes:
        tree.add_node(i)
    print(tree.repr())

