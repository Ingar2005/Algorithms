package main

type Stack struct {
	array []string
}

func (stack Stack) peek() string {
	arr := stack.array
	var ans string = ""
	if len(arr) <= 0 {
		return ans
	}
	ans = arr[(len(arr) - 1)]
	return ans
}
func (stack *Stack) push(val string) {
	stack.array = append(stack.array, val)
}
func (stack *Stack) pop() string {
	length := len(stack.array) - 1
	var val string = stack.array[length]
	stack.array = stack.array[0:length]
	return val
}
