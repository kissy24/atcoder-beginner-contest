package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func input() (int, int, int, int) {
	var sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	f := func() int {
		sc.Scan()
		i, _ := strconv.Atoi(sc.Text())
		return i
	}
	return f(), f(), f(), f()
}

func calc(N int, A int, X int, Y int) int {
	if N < A {
		return N * X
	} else {
		return A*X + (N-A)*Y
	}
}

func main() {
	fmt.Println(calc(input()))
}
