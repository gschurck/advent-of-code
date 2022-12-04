package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getInput(day int) *bufio.Scanner {
	pwd, _ := os.Getwd()
	b, err := os.ReadFile(pwd + "/day" + strconv.Itoa(day) + "/input.txt")
	if err != nil {
		fmt.Print(err)
	}
	str := string(b)
	println(str)
	return bufio.NewScanner(strings.NewReader(str))
}

func main() {

	var reindeers []int
	idRenne := 0
	inputScanner := getInput(1)
	for inputScanner.Scan() {
		println(inputScanner.Text())

		if inputScanner.Text() == "" {
			idRenne++
			continue
		} else if itemCalories, err := strconv.Atoi(inputScanner.Text()); err != nil {
			print("error", err)
			break
		} else if len(reindeers) > idRenne {
			reindeers[idRenne] += itemCalories
		} else {
			reindeers = append(reindeers, itemCalories)
		}

	}
	sort.Sort(sort.Reverse(sort.IntSlice(reindeers)))

	println("#1 Reindeer: ", reindeers[0])
	println("Top 3: ", sum(reindeers[:3]))
}

func sum(array []int) int {
	result := 0
	for _, v := range array {
		result += v
	}
	return result
}
