use std::fs::File;
use std::io::{BufRead, BufReader};
use slicestring::Slice;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let register = build_reg();
    20 * register[19] + 60 * register[59] + 100 * register[99] + 140 * register[139] + 180 * register[179] + 220 * register[219]
}

fn part2() -> String {
    let register = build_reg();

    let mut screen_out: String = String::new();

    for i in 0..register.len() {
        if (register[i]-1 <= i as i32 % 40) & ((i as i32 % 40) <= register[i] + 1) {
            screen_out += &"#".to_string();
        } else {
            screen_out += &".".to_string();
        }
    }

    screen_out
}


fn build_reg() -> Vec<i32> {
    let f = File::open("./input/data_10").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut register: Vec<i32> = Vec::new();
    register.push(1);
    
    for line in f.lines() {
        if let Ok(s) = line {
            let command: String = s.slice(..4);
            if command == "noop" {
                register.push(*register.last().unwrap());
            } else if command == "addx" {
                let to_add = s.slice(5..).parse::<i32>().unwrap();
                register.push(*register.last().unwrap());
                register.push(*register.last().unwrap() + to_add);
            }
        }
    }
    register
}