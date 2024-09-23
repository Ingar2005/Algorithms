package main

import "fmt"

type High struct {
	index int
	value int
}

func selection_sort(arr []int) []int {
	for i := (len(arr) - 1); i >= 0; i-- {
		high := High{index: -1, value: -1}
		for j := 0; j < i; j++ {
			val := arr[j]
			if val > high.value {
				high.value = val
				high.index = j
			}
		}
		if high.index != -1 {
			arr[high.index], arr[i] = arr[i], arr[high.index]
		}
	}
	return arr
}

func main() {
	fmt.Printf("%v", selection_sort([]int{3, 4, 6, 2, 1, 3, 4, 6, 8, 96, 5, 43, 23, 2, 1, 2, 34, 64, 64, 6, 7, 89, 0, 0, 0, 56, 3}))
}
