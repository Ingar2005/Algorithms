def selection_sort(arr) -> list:
    high = -1
    ind_high = -1
    for index in reversed(range(0,len(arr))):
        for s_index in range(0,index+1):
            val = arr[s_index]
            if val > high:
                high = val
                ind_high = s_index
        if ind_high != -1:
            temp = arr[index]
            arr[index] = high
            arr[ind_high] = temp
        high = -1
        ind_high = -1
    return arr

if __name__=="__main__":
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

    print(selection_sort(array) if array else "Please give a valid entry")
