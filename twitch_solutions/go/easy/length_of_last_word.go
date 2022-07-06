package main

func lengthOfLastWord(s string) int {
	length := 0
	word_started := false
	for i := len(s) - 1; i > -1; i-- {
		if s[i] == ' ' {
			if word_started {
				return length
			}
		} else {
			word_started = true
			length++
		}
	}
	return length
}
