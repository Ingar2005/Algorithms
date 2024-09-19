package main

func bubble_sort(arr []int) []int {
out:
	for i := 0; i < len(arr); i++ {
		var swap bool = false
		for x := 0; x < (len(arr) - 1); x++ {
			left := arr[x]
			right := arr[x+1]
			if left > right {
				arr[x], arr[x+1] = arr[x+1], arr[x]
				swap = true
			}

		}
		if swap == false {
			break out
		}

	}
	return arr

}
