use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;
use regex::Regex;

fn day1() -> io::Result<()> {
    let path = Path::new("src/bin/day3.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);

    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let mut result = 0;

    for line in reader.lines() {
        let line = line?;
        for (_, [n1, n2]) in re.captures_iter(&line).map(|c| c.extract()) {
            //println!("cap: {:?}", cap);
            let mult = n1.parse::<i32>().unwrap() * n2.parse::<i32>().unwrap();
            println!("Found match: {} * {} = {}", n1, n2, mult);
            result += mult;
        }
    }

    println!("Result {}", result);

    Ok(())
}

fn main() -> io::Result<()> {
    let path = Path::new("src/bin/day3.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);

    let re = Regex::new(r"(?P<mul>mul\((\d+),(\d+)\))|(?P<dont>don't)|(?P<do>do)").unwrap();

    let mut result = 0;

    let mut enabled = true;

    for line in reader.lines() {
        let line = line?;
        for cap in re.captures_iter(&line) {
            println!("cap: {:?}", cap);
            if cap.name("mul").is_some() && enabled {

                let n1: i32 = cap[2].parse().unwrap();
                let n2: i32 = cap[3].parse().unwrap();

                let mult = n1 * n2;

                println!("Found match: {} * {} = {}", n1, n2, mult);
                result += mult;
                continue
            }
            enabled = if cap.name("do").is_some() {
                true
            } else if cap.name("dont").is_some() {
                false
            } else {
                enabled
            }
        }
    }

    println!("Result {}", result);

    Ok(())
}