use std::cmp::max_by_key;
use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;
use std::str::Chars;

fn check_char(x: usize, y: usize, table: &Vec<Vec<char>>, mut iterator: Chars) -> bool {
    let char = table[y][x];
    match iterator.next() {
        Some(next_char) => char == next_char,
        None => true,
    }
}

fn move_x(direction: i32, x: usize, y: usize, table: &Vec<Vec<char>>, mut iterator: Chars) -> i32 {
    match check_char(x, y, table, iterator) {
        true => move_x(direction + x, y)
        false => 0
    }
}

fn move_y(direction: i32, x: i32, y: i32) -> (i32, i32) {
    (x, y + direction)
}

fn move_top_left_bot_right(direction: i32, x: i32, y: i32) -> (i32, i32) {
    (x - direction, y + direction)
}

fn move_bot_left_top_right(direction: i32, x: i32, y: i32) -> (i32, i32) {
    (x + direction, y + direction)
}

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
            println!("{}", letter);
            let xmas_iter = xmas.chars().into_iter();
            let test = check_char(x, y, &table, xmas_iter);
        }
    }

    Ok(())
}
