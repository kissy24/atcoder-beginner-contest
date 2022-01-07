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
func ParseArgs() (string, string) {
	optionPy := flag.String("py", ".py", "generate python file")
	optionGo := flag.String("go", ".go", "generate golang file")
	flag.Parse()
	return *optionPy, *optionGo
}

func GenerateFolder(stem string, extension string) {
	folderName := stem + extension
	os.Create(folderName)
}

func main() {
	fmt.Println(ParseArgs())
}
