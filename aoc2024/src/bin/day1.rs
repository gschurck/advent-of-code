use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn part1() -> io::Result<()> {
    // Specify the file path
    let path = Path::new("src/bin/day1.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);

    let mut left = Vec::new();
    let mut right= Vec::new();


    // Iterate over each line in the file
    for line in reader.lines() {
        let line = line?;
        // Split the line by whitespace and parse each part as a number
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();
        left.push(numbers[0]);
        right.push(numbers[1]);

        // Print the numbers
        println!("{:?}", numbers);
    }

    left.sort();
    right.sort();

    let mut sum = 0;
    for (l, r) in left.iter().zip(right.iter()) {
        println!("Left: {}, Right: {}", l, r);
        let distance = (l-r).abs();
        println!("Distance: {}", distance);
        sum += distance
    }

    println!("Total {}", sum);

    Ok(())
}

fn main() -> io::Result<()> {
    // Specify the file path
    let path = Path::new("src/bin/day1.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);

    let mut left = HashMap::new();
    let mut right = HashMap::new();


    // Iterate over each line in the file
    for line in reader.lines() {
        let line = line?;
        // Split the line by whitespace and parse each part as a number
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();
        *left.entry(numbers[0]).or_insert(0) += 1;
        *right.entry(numbers[1]).or_insert(0) += 1;

        // Print the numbers
        println!("{:?}", numbers);
    }

    let mut sum = 0;
    for number in left.keys(){
        let similarity = number * right.get(number).unwrap_or(&0);
        sum += similarity
    }

    println!("Total {}", sum);

    Ok(())
}