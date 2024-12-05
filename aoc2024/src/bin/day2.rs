use std::cmp::Ordering;
use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;

#[derive(PartialEq)]
enum Type {
    Increasing,
    Decreasing,
}

fn is_safe(line_type: &Type, first_number: i32, second_number: i32) -> bool {
    println!("between {} and {}", first_number, second_number);
    (Type::Increasing == *line_type && first_number < second_number && second_number - first_number <= 3)
        || (Type::Decreasing == *line_type && first_number > second_number && first_number - second_number <= 3)
}

fn day1() -> io::Result<()> {
    let path = Path::new("src/bin/day2.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);


    let mut sum = 0;

    for (id, line) in reader.lines().enumerate() {
        let line = line?;
        // Split the line by whitespace and parse each part as a number
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();

        println!("{:?}", numbers);


        let mut last_number = numbers[0];
        let line_type = if last_number < numbers[1] {
            Type::Increasing
        } else if last_number > numbers[1] {
            Type::Decreasing
        } else {
            continue
        };
        let mut safe = is_safe(&line_type, last_number, numbers[1]);
        if !safe {
            continue
        }
        last_number = numbers[1];
        for i in 2..numbers.len() {
            let number = numbers[i];
            if !is_safe(&line_type, last_number, number) {
                safe = false;
                break
            }
            last_number = number;
        }
        if safe {
            sum += 1;
            println!("{} is safe", id)
        }
    }
    println!("Total {}", sum);


    Ok(())
}

fn get_line_type(a: i32, b: i32) -> Option<Type> {
    match a.cmp(&b) {
        Ordering::Less => Some(Type::Increasing),
        Ordering::Greater => Some(Type::Decreasing),
        Ordering::Equal => None,
    }
}

fn line_is_safe(numbers: &[i32]) -> bool {
    if let Some(line_type) = get_line_type(numbers[0], numbers[1]) {
        numbers
            .windows(2)
            .all(|pair| is_safe(&line_type, pair[0], pair[1]))   
    } else {
        false
    }
}

fn main() -> io::Result<()> {
    let path = Path::new("src/bin/day2.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);


    let mut sum = 0;

    for (id, line) in reader.lines().enumerate() {
        let line = line?;
        // Split the line by whitespace and parse each part as a number
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().expect("parse error"))
            .collect();

        println!("{:?}", numbers);


        let mut safe = line_is_safe(&numbers);
        
        if !safe {
            for i in 0..numbers.len() {
                let mut numbers_cloned = numbers.clone();
                numbers_cloned.remove(i);
                if line_is_safe(&numbers_cloned) {
                    safe = true;
                    break
                }
            }
        }
        
        if safe {
            sum += 1;
            println!("{} is safe", id)
        }
    }
    println!("Total {}", sum);


    Ok(())
}
