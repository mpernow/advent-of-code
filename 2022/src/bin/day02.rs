use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let mut total: u32 = 0;
    let f = File::open("./input/data_02").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            let turn_tup = (s.chars().nth(0).unwrap(), s.chars().nth(2).unwrap());
            let turn_tup_num = transform_numeric(turn_tup);
            total = total + calc_score(turn_tup_num) as u32;
        }
    }
    total
}

fn part2() -> u32 {
    let mut total: u32 = 0;
    let f = File::open("./input/data_02").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            let turn_tup = (s.chars().nth(0).unwrap(), s.chars().nth(2).unwrap());
            let turn_tup_num = transform_numeric(turn_tup);
            total = total + calc_score2(turn_tup_num);
        }
    }
    total
}

fn calc_score2(tup: (u32, u32)) -> u32 {
    let outcome: i32 = tup.1 as i32;
    let opp: i32 = tup.0 as i32;

    let score = outcome * 3;
    let score = score + 1 + match outcome {
        0 => (((opp - 1) % 3) + 3) % 3,
        1 => opp,
        2 => (opp + 1) % 3,
        _ => 0
    };

    score as u32
}

fn calc_score(tup: (u32, u32)) -> i32 {
    let mine: i32 = tup.1 as i32;
    let opp: i32 = tup.0 as i32;

    let diff = mine - opp;

    let score = mine + 1;
    let score = score + match ((diff % 3) + 3) % 3 {
        0 => 3,
        1 => 6,
        2 => 0,
        _ => 0
    };

    score
}

fn transform_numeric(turn_tup: (char, char)) -> (u32, u32) {
    let v1: u32 = match turn_tup.0 {
        'A' => 0,
        'B' => 1,
        'C' => 2,
        _ => 3
    };

    let v2: u32 = match turn_tup.1 {
        'X' => 0,
        'Y' => 1,
        'Z' => 2,
        _ => 3
    };

    (v1, v2)
}