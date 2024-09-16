package main

import "fmt"

func linear_search(arr []string, target string) int {
	index := -1
out:
	for i := 0; i < len(arr); i++ {
		if arr[i] == target {
			index = i
			break out
		}
	}
	return index
}

func main() {
	var arr []string
	var its int
	var targ string
	fmt.Println("enter the amount of values you wish to enter")
	fmt.Scan(&its)
	for i := 0; i < its; i++ {
		temp := ""
		fmt.Println("enter a value if you are finished press enter")
		fmt.Scan(&temp)
		arr = append(arr, temp)

	}
	fmt.Println("enter the value you ant to find")
	fmt.Scan(&targ)

	fmt.Printf(" target: %v \n index found: %v \n", targ, linear_search(arr, targ))
}
