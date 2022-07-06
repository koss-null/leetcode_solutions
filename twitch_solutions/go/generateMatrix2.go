package main

func generateMatrix(n int) [][]int {
	leftShift, rightShift, topShift, bottomShift := 0, 0, 0, 0
	direction := 1 // 1: -> 2: V 3: <- 4: ^
	i := 1

	res := make([][]int, n)
	for j := range res {
		res[j] = make([]int, n)
	}

	for i <= n*n {
		switch direction {
		case 1:
			for j := leftShift; j < n-rightShift; j++ {
				res[topShift][j] = i
				i++
			}
			topShift++
			direction = 2
		case 2:
			for j := topShift; j < n-bottomShift; j++ {
				res[j][n-rightShift-1] = i
				i++
			}
			rightShift++
			direction = 3
		case 3:
			for j := n - rightShift - 1; j > leftShift-1; j-- {
				res[n-rightShift][j] = i
				i++
			}
			bottomShift++
			direction = 4
		case 4:
			for j := n - bottomShift - 1; j > topShift-1; j-- {
				res[j][leftShift] = i
				i++
			}
			leftShift++
			direction = 1
		}
	}
	return res
}
