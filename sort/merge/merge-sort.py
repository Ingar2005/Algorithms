def merge_sort(arr) -> list:
    midpoint = (len(arr) // 2)
    if len(arr) == 1:
        return arr
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])
    sorted =[]
    while left and right:
        if (left[0] <= right[0]):
            sorted.append(left[0])
            left = left[1:]
        else:
            sorted.append(right[0])
            right = right[1:]
        if left == []:
            for num in right:
                sorted.append(num)
        elif right == []:
            for num in left:
                sorted.append(num)
    return sorted

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

    print(merge_sort(array) if array else "Please give a valid entry")
