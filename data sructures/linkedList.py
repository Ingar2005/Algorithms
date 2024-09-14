class linked_list:

    def __init__(self):
        self.start = -1
        self.size = -1

    def add_item(self,item=None)->None:
        if isinstance(item,node):
            if self.start == -1:
                self.start = item
            else:
                next = self.start
                while True:
                    if next.pointer ==-1:
                        next.pointer = item
                        self.size +=1
                        break
                    else:
                        next = next.pointer

    def delete(self,index):
        if index == 0:
            hold = self.start
            self.start = self.start.pointer if self.start.pointer != -1 else -1
            return hold
        next = self.start
        if self.size < index:
            raise Exception("out of index")
        next = self.start
        cur_index = 0
        while cur_index < (index-1):
            next = next.pointer
            cur_index += 1
        before = next
        middle = next.pointer
        end = middle.pointer
        before.set_pointer(end)
            

    def return_all(self)->list:
        if self.start == -1:
            return None
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
        if isinstance(item,node) or item == -1 :
            self.pointer = item

if __name__ =="__main__":
    list= linked_list()
    for i in range(0,6):
        list.add_item(node(i))
    print(list.return_all())
    list.delete(1)
    print(list.return_all())
   

