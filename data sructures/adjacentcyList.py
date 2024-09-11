class linked_list:

    def __init__(self):
        self.start = -1

    def add_item(self,item=None)->None:
        if isinstance(item,node):
            if self.start == -1:
                self.start = item
            else:
                next = self.start
                while True:
                    if next.pointer ==-1:
                        next.pointer = item
                        break
                    else:
                        next = next.pointer
    def return_all(self)->list:
        if self.start == -1:
            print( None)
        next = self.start
        arr = []
        while True:
            if next.pointer ==-1:
                arr.append(next.data)
                break
            else:
                arr.append(next.data)
                next = next.pointer
        return (arr)

                
class node:

    def __init__(self,data,pointer=-1):
        self.data = data
        self.pointer = pointer
    def set_pointer(self,item):
        if isinstance(item,list_node):
            self.pointer = item

