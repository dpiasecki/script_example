package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {

	if len(os.Args) == 1 {
		fmt.Println("first input is missing")
		os.Exit(0)
	} else if len(os.Args) == 2 {
		fmt.Println("second input is missing")
		os.Exit(0)
	}

	first, err1 := strconv.Atoi(os.Args[1])
	second, err2 := strconv.Atoi(os.Args[2])

	if err1 != nil {
		fmt.Println("first input is not a number.")
		os.Exit(0)
	} else if err2 != nil {
		fmt.Println("second input is not a number.")
		os.Exit(0)
	}

	fmt.Println(first + second)

}
