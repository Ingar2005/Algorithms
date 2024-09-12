arr = [4,3,6,2,1,6]


class Heap:

    def __init__(self,arr=[],type=None):
        if arr ==[] or type == None or not (type == "max" or type == "min"):
            raise Exception("the heap pooded its pants due to a lack of type or a lack of an array you find out which one becouse i am busy")
        self.__type = type
        self.__heap = arr
        for i in reversed(range(0,len(arr))):
            self.__heap = self.__heapify(arr,len(arr),i)
    
    def __heapify(self,arr,size,root=0,*h):
        ind_big = root
        child_l, child_r = (root*2)+1, (root*2)+2
            
        if child_l < (size) and arr[child_l]>arr[ind_big]:
            ind_big = child_l
        elif child_r<(size) and arr[child_r]>arr[ind_big]:
            ind_big = child_r
        if ind_big != root:
            arr[root], arr[ind_big] = arr[ind_big], arr[root]
            self.__heapify(arr,size,root)

    def add(self,val):
        if not isinstance(val,(int,float)):
            raise Exception("the vlaue you tried to add is not numeric")
        self.__heap.append(val)
        self.__heapify(self.__heap)

    # def __repr__(self) -> str:
    #     string = ""
    #     for index in range(0, len(self.__heap)):
    #         string +=(f"index: {index+1} value: {self.__heap[index]} \n")
    #     return string

                


if __name__ == "__main__":
    heap = Heap([4,3,6,2,1,6],"max")
    print(heap)
    