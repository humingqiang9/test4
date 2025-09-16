package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

func printNumber(num int, ch chan bool) {
	fmt.Println(num)
	ch <- true
}

func main() {
	rand.Seed(time.Now().UnixNano())
	filename := fmt.Sprintf("random_output_%d.txt", rand.Intn(10000))
	fmt.Printf("Writing to file: %s\n", filename)

	// Create file
	file, err := os.Create(filename)
	if err != nil {
		fmt.Println("Error creating file:", err)
		return
	}
	defer file.Close()

	// Duplicate stdout to originalStdout
	originalStdout := os.Stdout
	defer func() { os.Stdout = originalStdout }()

	// Redirect stdout to file
	os.Stdout = file

	ch := make(chan bool)

	for i := 1; i <= 10; i++ {
		go printNumber(i, ch)
	}

	for i := 1; i <= 10; i++ {
		<-ch
	}
}