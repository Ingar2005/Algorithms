arr = [8,81,23,4,8,6,2,5,4,7,5,2,4]
def partition(arr,l,h) -> (list):
    # l is low h is high representing the lowest/ highest index
    pivot = arr[l]
    i ,j = l,h
    while i<j:
        while arr[i] <= pivot:
            i +=1
        while arr[j] > pivot:
            j -=1
        if i <j:
            arr[i],arr[j] = arr[j],arr[i]
            #new way of swaping elements
    arr[l], arr[j] = arr[j], arr[l]
    return (j)

def quick_sort(arr,l=0,h=None) -> list:
    if h ==None:
        h=len(arr)
    if l<h:
        j = partition(arr,l,h-1)
        quick_sort(arr,l,j)
        quick_sort(arr,j+1,h)
if __name__ =="__main__":
    print(quick_sort(arr))
    print(arr)