package main

func binarySearch(arr []int, target int, start int) int {
	if len(arr) <= 0 {
		return -1
	}
	var midpoint int = len(arr) / 2
	if arr[midpoint] == target {
		return midpoint + start
	} else if arr[midpoint] > target {
		return binarySearch(arr[:midpoint], target, start)
	} else if arr[midpoint] < target {
		return binarySearch(arr[midpoint:], target, midpoint+start)
	}
	return -1
}
