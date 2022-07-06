func plusOne(digits []int) []int {
	mem := true
	for i := len(digits) - 1; i > -1; i-- {
		if mem {
			sum := digits[i] + mem
			if sum < 10 {
				mem = false
			}
			digits[i] = sum % 10
		}
		break
	}
	if mem {
		return append([]int{1}, digits...)
	}
	return digits
}
