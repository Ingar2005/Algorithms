def insertion_sort(arr) -> list:
    for index in range(1,len(arr)):
        swap = True
        ind = index
        s_index= index-1
        while swap == True and s_index >= 0:
            if arr[ind] < arr[s_index]:
                temp = arr[ind]
                arr[ind] = arr[s_index]
                arr[s_index] = temp
                ind -=1
                s_index -=1
            else:
                swap = False
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

    print(insertion_sort(array) if array else "Please give a valid entry")
