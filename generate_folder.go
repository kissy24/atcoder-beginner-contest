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

// Generates a folder and files with the given name and extension
func GenerateFolder(num string, extension string) {
	folderName := "ABC_" + num
	if err := os.Mkdir(folderName, 0777); err != nil {
		fmt.Println(err)
	}
	os.Create(folderName)
	stems := [4]string{"a", "b", "c", "d"}
	for _, stem := range stems {
		os.Create(folderName + "/" + stem + extension)
	}
}

func main() {
	folderName := Input()
	extension := ParseArgs()
	GenerateFolder(folderName, extension)

}
