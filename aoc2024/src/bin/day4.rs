use crate::State::{GoodChar, GoodWord, WrongChar};
use std::fs::File;
use std::io;
use std::io::BufRead;
use std::path::Path;
use std::str::Chars;

enum State {
    WrongChar,
    GoodChar,
    GoodWord,
}

fn check_char(x: usize, y: usize, table: &Vec<Vec<char>>, iterator_value: Option<char>) -> State {
    if let Some(row) = table.get(y) {
        if let Some(&char) = row.get(x) {
            match iterator_value {
                Some(next_char) => {
                    if char == next_char {
                        GoodChar
                    } else {
                        WrongChar
                    }
                }
                None => GoodWord,
            }
        } else {
            WrongChar
        }
    } else {
        WrongChar
    }
}

#[derive(Clone, Copy)]
enum Direction {
    Horizontal(isize),      // Left/Right
    Vertical(isize),        // Up/Down
    Diagonal(isize, isize), // (x_delta, y_delta)
}

fn move_in_direction<'a>(
    dir: Direction,
    x: usize,
    y: usize,
    table: &Vec<Vec<char>>,
    mut iterator: Chars<'a>,
) -> (i32, Chars<'a>) {
    match check_char(x, y, table, iterator.next()) {
        WrongChar => {
            return (0, iterator);
        }
        GoodChar => (),
        GoodWord => return (1, iterator),
    }

    match dir {
        Direction::Horizontal(dx) => {
            move_in_direction(dir, (x as isize + dx) as usize, y, table, iterator)
        }
        Direction::Vertical(dy) => {
            move_in_direction(dir, x, (y as isize + dy) as usize, table, iterator)
        }
        Direction::Diagonal(dx, dy) => move_in_direction(
            dir,
            (x as isize + dx) as usize,
            (y as isize + dy) as usize,
            table,
            iterator,
        ),
    }
}

fn move_all_in_direction(
    direction: isize,
    x: usize,
    y: usize,
    table: &Vec<Vec<char>>,
    xmas: &str,
) -> i32 {
    let mut sum = 0;
    // Previous move_x becomes:
    sum += move_in_direction(Direction::Horizontal(direction), x, y, table, xmas.chars()).0;

    // Previous move_y becomes:

    sum += move_in_direction(Direction::Vertical(direction), x, y, table, xmas.chars()).0;

    // Previous move_top_left_bot_right becomes:
    sum += move_in_direction(
        Direction::Diagonal(-direction, direction),
        x,
        y,
        table,
        xmas.chars(),
    )
    .0;

    // Previous move_bot_left_top_right becomes:
    sum += move_in_direction(
        Direction::Diagonal(direction, -direction),
        x,
        y,
        table,
        xmas.chars(),
    )
    .0;

    sum
}

fn main() -> io::Result<()> {
    let path = Path::new("src/bin/day4.txt");

    // Open the file
    let file = File::open(&path)?;
    let xmas = "XMAS";

    let reader = io::BufReader::new(file);
    let table: Vec<Vec<char>> = reader
        .lines()
        .map(|line| line.unwrap().chars().collect())
        .collect();

    let mut sum = 0;

    for (y, line) in table.iter().enumerate() {
        for (x, letter) in line.iter().enumerate() {
            //println!("{}", letter);
            sum += move_all_in_direction(1, x, y, &table, xmas);
            sum += move_all_in_direction(-1, x, y, &table, xmas);
        }
    }

    println!("Result {}", sum);

    Ok(())
}
