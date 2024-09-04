def bubble_sort(arr)-> list:
    if len(arr) <= 0:
        return []
    for index in range(0,len(arr)):
        correct = False
        for curr in range(0,len(arr)-1):
            if arr[curr] >= arr[curr+1]:
                temp = arr[curr+1]
                arr[curr+1] = arr[curr]
                arr[curr] = temp
    return arr

if __name__ == "__main__":
    array = []
    while True:
        temp = input("Enter a value into the array (press enter to finish): \n")
        try:
            if temp:
                array.append(int(temp))
            else:
                break
        except:
            print("integers only please")
    print(bubble_sort(array))
