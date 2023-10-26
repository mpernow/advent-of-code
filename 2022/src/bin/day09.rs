use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use slicestring::Slice;


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_09").expect("Unable to open file");
    let f = BufReader::new(f);
    
    let mut head: (i32, i32) = (0, 0);
    let mut tail: (i32, i32) = (0, 0);
    let mut positions: HashSet<(i32, i32)> = HashSet::new();
    positions.insert(tail);

    for line in f.lines() {
        if let Ok(s) = line {
            let direction: String = s.slice(..1);
            let steps: i32 = s.slice(2..).parse::<i32>().unwrap();
            for _i in 0..steps {
                head = move_head(head, direction.clone());
                tail = move_tail(tail, head);
                positions.insert(tail);
            }
        }
    }
    positions.len().try_into().unwrap()
}

fn part2() -> u32 {
    let f = File::open("./input/data_09").expect("Unable to open file");
    let f = BufReader::new(f);
    
    let mut knots: Vec<(i32, i32)> = Vec::new();
    for _i  in 0..10 {
        let pos: (i32, i32) = (0, 0);
        knots.push(pos);
    }
    let mut positions: HashSet<(i32, i32)> = HashSet::new();
    positions.insert(knots[9]);

    for line in f.lines() {
        if let Ok(s) = line {
            let direction: String = s.slice(..1);
            let steps: i32 = s.slice(2..).parse::<i32>().unwrap();
            for _i in 0..steps {
                knots[0] = move_head(knots[0], direction.clone());
                for i in 1..10 {
                    knots[i] = move_tail(knots[i], knots[i-1]);
                }
                positions.insert(knots[9]);
            }
        }
    }
    positions.len().try_into().unwrap()
}

fn move_head(head: (i32, i32), direction: String) -> (i32, i32) {
    let mut new_head = (head.0, head.1);
    if direction == "U" {
        new_head.1 += 1;
    } else if direction == "D" {
        new_head.1 -= 1;
    } else if direction == "R" {
        new_head.0 += 1;
    } else if direction == "L" {
        new_head.0 -= 1;
    }
    new_head
}

fn move_tail(tail: (i32, i32), head: (i32, i32)) -> (i32, i32) {
    let mut new_tail = (tail.0, tail.1);
    let diff = (head.0 - tail.0, head.1 - tail.1);
    if (diff.0.abs() <= 1) & (diff.1.abs() <= 1) {
        // Do nothing
    } else if diff.0 == 0 {
        // Move tail in y-direction
        new_tail.1 += diff.1.signum();
    } else if diff.1 == 0 {
        // Move tail in x-direction
        new_tail.0 += diff.0.signum();
    } else {
        // Move diagonally
        new_tail.0 += diff.0.signum();
        new_tail.1 += diff.1.signum();
    }
    new_tail
}