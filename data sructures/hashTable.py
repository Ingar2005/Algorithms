from linkedList import linked_list as Llist
from linkedList import node as Node

class HashTable:

    def __init__(self,size):
        if size <= 0:
            raise Exception("size must be at least 1")
        self.__table = []
        for i in range(0,size):
            self.__table.append(Llist())
        self.__size = size
    
    def __hashfunc(self,val):
        key  = hash(val) % self.__size
        return abs(key)

    def add(self,val):
        #if type(val) == list:
        #    raise Exception("no lists please")
        key = self.__hashfunc(val) 
        value = Node(val)
        list = Llist()
        list.add_item(value)
        self.__table[key] = list
    
    def delete(self,val):
        res = self.__find(val)
        if res[0] == None:
            raise Exception("not found")
        list = self.__table[res[0]]
        list.delete(res[1])
        self.__table[res[0]] = list


    def __find(self,val) -> tuple:
        key = self.__hashfunc(val)
        list = self.__table[key]
        list = list.return_all()
        for i in range(0,len(list)):
            if list[i] == val:
                return (key,i)
        return (None,None)

    def __repr__(self):
        arr = []
        str = ""
        for i in self.__table: 
            arr.append(i.return_all())
        for i in range(0,len(arr)):
            str += f"index: {i} linked list: {arr[i]} \n"
        return str


if __name__ =="__main__":
    table = HashTable(5)
    table.add(4)
    table.add(2)
    table.add(3)
    print(table)
    table.delete(2)
    print(table)
