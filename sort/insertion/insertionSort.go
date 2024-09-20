package main

func insertion_sort(arr []int) []int {
	if len(arr) <= 0 {
		return []int{}
	}

	for index := 1; index < len(arr); index++ {
	out:
		for temp_index, second_index := index, index-1; second_index > 0; temp_index, second_index = temp_index-1, second_index-1 {
			var left int = arr[second_index]
			var right int = arr[temp_index]
			if left > right {
				arr[second_index], arr[temp_index] = right, left
			} else {
				break out
			}
		}
	}
	return arr

}
