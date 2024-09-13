
def binary_search(arr,val,start_val=0) -> int:
    if not arr and not val:
        return -1
    midpoint = (len(arr) ) // 2
    if arr[midpoint]== val:
        return midpoint+start_val
    elif arr[midpoint] > val:
        return binary_search(arr[:midpoint],val,start_val)
    elif arr[midpoint] < val:
        return binary_search(arr[midpoint:],val,midpoint+start_val)

    

if __name__ =="__main__":
    array = []
    while True:
        try:
            temp = input("Enter a value into the array (press enter to finish): \n")
            if temp:
                if array == [] or array[-1] <= int(temp):
                    array.append(int(temp))
                else:
                    print("numbers must be in accending order")
            else:
                break
        except Exception as exc:
            print("only numerical values \n Error: \n",exc)
    while True:
        value = input("What value would you like to find: \n")
        if value.isnumeric():
            value = int(value)
            break
        else:
            print("must be numerical")

    res = binary_search(array,value)
    print(f"Original: {array} \n Index: ")
    print(res if res != -1 else "Not found")
