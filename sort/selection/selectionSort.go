package main

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
