package main

import "fmt"

func merge_sort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}
	midpoint := len(arr) / 2
	left := merge_sort(arr[:midpoint])
	right := merge_sort(arr[midpoint:])
	sorted := []int{}
out:
	for {
		if left[0] >= right[0] {
			sorted = append(sorted, right[0])
			right = right[1:]

		} else if left[0] < right[0] {
			sorted = append(sorted, left[0])
			left = left[1:]
		}
		if len(left) <= 0 {
			for nums := 0; nums < len(right); nums++ {
				sorted = append(sorted, right[nums])
			}
			break out
		}
		if len(right) <= 0 {
			for nums := 0; nums < len(left); nums++ {
				sorted = append(sorted, left[nums])
			}
			break out
		}
	}
	return sorted
}

func main() {
	fmt.Printf("%v ", merge_sort([]int{4, 5, 6, 23, 4, 2, 3, 5, 7, 9, 5, 3, 5, 7, 88, 3, 2, 432, 1, 0}))
}
