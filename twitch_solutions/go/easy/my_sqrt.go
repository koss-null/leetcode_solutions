package main

import "fmt"

// fixme: this is slow
func pow(a, b int) int {
	switch {
	case a == 0:
		return 0
	case b == 0:
		return 1
	}

	res := 1
	for b != 0 {
		res *= a
		b--
	}

	return res
}

func fact(a int) int {
	res := 1
	for i := 1; i < a; i++ {
		res *= i
	}
	return res
}

func mySqrt(x int) int {
	res := float32(0)
	x -= 1
	for n := 1; n < 50; n++ {
		res += float32(pow(-1, n)*fact(2*n)*pow(x, n)) / float32((1-2*n)*pow(fact(n), 2)*pow(4, n))
		fmt.Println(res)
	}
	return int(res)
}

func main() {
	fmt.Println(mySqrt(256))
}
