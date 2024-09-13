

class Heap:

    def __init__(self):
        self.__heap = []


    def __sort(self):
        arr = self.__heap
        for i in range(len(arr),-1,-1):
            self.__heapify(i)


    def add(self,val):
        if not isinstance(val,(int,float)):
            raise Exception("the vlaue you tried to add is not numeric")
        self.__heap.append(val)
        self.__sort()

    def delete(self):
        arr = self.__heap
        root = 0
        val = arr.pop(0)
        self.__heap = arr
        self.__sort()
        return val
        

    def __heapify(self,root):
        arr = self.__heap
        big = root
        child_l = root*2 +1 if (len(arr)-1) >= root*2+1 else None
        child_r = root*2 +2 if (len(arr)-1) >= root*2+2 else None
        
        if child_l!= None and arr[child_l] > arr[big]:
            big = child_l
        if child_r!= None and arr[child_r] > arr[big]:
            big = child_r

        if big != root:
            arr[big],arr[root] = arr[root],arr[big]
        self.__heap = arr

    def __repr__(self) -> str:
         string = ""
         for index in range(0, len(self.__heap)):
             string +=(f"index: {index+1} value: {self.__heap[index]} \n")
         return string

                



