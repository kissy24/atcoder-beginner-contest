package main

import (
	"fmt"
	"strings"
)

func input() string {
	var s string
	fmt.Scan(&s)
	return s
}

func isUpperCase(alphabet string) string {
	var upAlphabet string = strings.ToUpper(alphabet)
	if alphabet == upAlphabet {
		return "A"
	} else {
		return "a"
	}
}

func main() {
	alphabet := input()
	isUpperStr := isUpperCase(alphabet)
	fmt.Println(isUpperStr)
}
