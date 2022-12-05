package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var rules = [3]rune{'A', 'B', 'C'}
var points int

func main() {
	for _, r := range rules {
		fmt.Printf("%v wins against %v\n", string(rules[getId(r)]), string(winsAgainst(r)))
		fmt.Printf("%v loses against %v\n", string(rules[getId(r)]), string(losesAgainst(r)))
	}

	inputScanner := getInputForDay(2)

	for inputScanner.Scan() {
		//println(inputScanner.Text())
		runes := []rune(inputScanner.Text())
		if len(runes) < 3 {
			continue
		}
		processRound(runes[0], runes[2])
	}

	fmt.Printf("\nPoints: %v\n", points)
}

func processRound(letter1 rune, letter2 rune) {
	var expectedLetter rune
	// Star #2
	switch letter2 {
	case 'X':
		expectedLetter = winsAgainst(letter1)
	case 'Y':
		expectedLetter = letter1
	case 'Z':
		expectedLetter = losesAgainst(letter1)
	}

	letter2 = expectedLetter
	letter2Id := getId(letter2)
	letter2 = rules[letter2Id]
	loserLetter := winsAgainst(letter2)
	if loserLetter == letter1 {
		points += 6
	} else if letter1 == letter2 {
		points += 3
	}
	points += letter2Id + 1
}

func getId(letter rune) int {
	i := letter - 65
	i = i % 23
	return int(i)
}

func winsAgainst(letter rune) rune {
	id := getId(letter)
	opponentId := mod(id-1, 3)
	return rules[opponentId]
}

func losesAgainst(letter rune) rune {
	id := getId(letter)
	opponentId := (id + 1) % 3
	return rules[opponentId]
}

func getInputForDay(day int) *bufio.Scanner {
	pwd, _ := os.Getwd()
	b, err := os.ReadFile(pwd + "/day" + strconv.Itoa(day) + "/input.txt")
	if err != nil {
		fmt.Print(err)
	}
	str := string(b)
	return bufio.NewScanner(strings.NewReader(str))
}

func mod(a, b int) int {
	return (a%b + b) % b
}
