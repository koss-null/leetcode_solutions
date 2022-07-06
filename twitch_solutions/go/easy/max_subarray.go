package main

import "fmt"

func maxSubArray(nums []int) int {
	s := make([]int, 0, len(nums)+1)
	for i, n := range nums {
		prev := 0
		if i != 0 {
			prev = s[i-1]
		}
		s = append(s, prev+n)
	}

	min, max := 1<<19, -1<<19
	for _, pref := range s {
		if pref < min {
			min = pref
		}
		if pref+min > max {
			max = pref + min
		}
	}

	return max
}

func main() {
	fmt.Println(maxSubArray([]int{1, 2, 3, 4, 5, -6, 7}))
}
