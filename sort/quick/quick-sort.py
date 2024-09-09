
def quick_sort(arr) -> list:    
    right_border = len(arr) -1
    indx_locked =[]
    for index in range(0,len(arr)):
        while True:
            midpoint = len(arr)//2
            if midpoint not in indx_locked:
                break
            else:
                for index in range(0,len(arr)):
                    midpoint = index
                    if midpoint not in indx_locked:
                        break
                break
        value = arr[midpoint]
        left_pnt = -1
        right_pnt = -1
        cross = False
        
        arr[midpoint] = arr[right_border]
        arr[right_border] = value
        # i have chosen the pivot and swaped it to the end of the arr 
        # aswell as this i have initiated the left and right value to -1
        for left_index in range(0,right_border):
            if arr[left_index] >= value and left_index not in indx_locked:
                left_pnt = left_index
                break
        for right_index in reversed(range(left_pnt,right_border)):
            if left_pnt == right_index:
                cross = True
                break
            if arr[right_index] < value and right_index not in indx_locked:
                right_pnt = right_index
                break
        if cross == True:
            temp = left_pnt
            arr[right_border] = arr[left_pnt]
            arr[left_pnt] = temp
            indx_locked.append(left_pnt)
        else:
            temp = arr[left_pnt]
            arr[left_pnt] = arr[right_pnt]
            arr[right_pnt] = temp

    return arr
        # i now find the left pointer and right pointer left will be larrger than pivot
        # and right should be smaller than pivot
        # if the values cross it activates cross and  
    
if __name__ =="__main__":
    print(quick_sort([8,81,23,4,8,6,2,5,4,7,5,2,4]))
