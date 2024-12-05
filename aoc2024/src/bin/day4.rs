use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;

fn main() -> io::Result<()> {
    let path = Path::new("src/bin/day4.txt");

    // Open the file
    let file = File::open(&path)?;
    let xmas = "XMAS";

    let mut table: Vec<Vec<char>> = Vec::new();

    let reader = io::BufReader::new(file);
    let table: Vec<Vec<char>> = reader
        .lines()
        .map(|line| line.unwrap().chars().collect())
        .collect();

    for (y, line) in table.iter().enumerate() {
        for (x, letter) in line.iter().enumerate() {
            println!("{}", letter)
        }
    }

    Ok(())
}
