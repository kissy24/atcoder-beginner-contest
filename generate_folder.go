package main

import (
	"flag"
	"fmt"
	"os"
)

// Prompts the user for the folder name
func Input() string {
	var s string
	fmt.Scan(&s)
	return s
}

// Parses the command line arguments
func ParseArgs() string {
	optLang := flag.String("lang", "py", "The language extension(ex. py, go, etc.)")
	flag.Parse()
	return "." + *optLang
}

func GenerateFolder(num string, extension string) {
	folderName := "ABC_" + num
	if err := os.Mkdir(folderName, 0777); err != nil {
		fmt.Println(err)
	}
	os.Create(folderName)
	var stems [4]string = [4]string{"a", "b", "c", "d"}
	for i := 0; i < 4; i++ {
		os.Create(folderName + "/" + stems[i] + extension)
	}
}

func main() {
	folderName := Input()
	extension := ParseArgs()
	GenerateFolder(folderName, extension)
}
