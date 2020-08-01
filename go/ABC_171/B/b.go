package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func stringToInt(ss []string) []int {
	var seq []int
	for _, s := range ss {
		i, _ := strconv.Atoi(s)
		seq = append(seq, i)
	}
	return seq

}

func input() (int, []int) {
	stdin := bufio.NewScanner(os.Stdin)
	stdin.Scan()
	nk := stdin.Text()
	nkSplit := strings.Split(nk, " ")
	k := nkSplit[1]
	kInt, _ := strconv.Atoi(k)
	stdin.Scan()
	p := stdin.Text()
	pSplit := strings.Split(p, " ")
	seq := stringToInt(pSplit)
	return kInt, seq
}

func main() {
	k, p := input()
	output := 0
	sort.Sort(sort.IntSlice(p))
	for i := 0; i < k; i++ {
		output += p[i]
	}
	fmt.Println(output)

}
