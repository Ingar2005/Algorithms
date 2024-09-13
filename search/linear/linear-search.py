def linear_search(arr=[1,2,3,4,5],find=5) -> int:
    position = None
    if arr and find:
      for index in range(0,len(arr)):
            if arr[index] == find:
                position = index
                break
    return position

if __name__ == "__main__":
    array = []
    while True:
        temp = input("Enter a value into the array (press enter to finish): \n")
        if temp:
            array.append(temp)
        else:
            break
    value = input("What value would you like to find: \n")
    res = linear_search(array,value)
    print(res if res != None else "Not found")
