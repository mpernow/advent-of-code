use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use slicestring::Slice;
use itertools::Itertools;


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let mut total: u32 = 0;
    let f = File::open("./input/data_03").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            let len = s.chars().count();
            let first = s.slice(..len/2);
            let second = s.slice(len/2..);
            let mut first_set = HashSet::new();
            for c in first.chars() {
                first_set.insert(c);
            }
            let mut second_set = HashSet::new();
            for c in second.chars() {
                second_set.insert(c);
            }
            let common: HashSet<_> = first_set.intersection(&second_set).collect();
            let mut priority: u32 = 0;
            for c in common {
                let c_char: char = *c;
                if c_char.is_uppercase() {
                    priority = priority + c_char.to_ascii_lowercase() as u32 - 70;
                } else if c_char.is_lowercase() {
                    priority = priority + c_char.to_ascii_uppercase() as u32 - 64;
                }
            }
            total = total + priority;
        }
    }
  total 
}

fn part2() -> u32 {
    let mut total: u32 = 0;
    let f = File::open("./input/data_03").expect("Unable to open file");
    let f = BufReader::new(f);

    for lines in &f.lines().chunks(3) {
        let mut first_set = HashSet::<char>::new();
        let mut second_set = HashSet::<char>::new();
        let mut third_set = HashSet::<char>::new();
        
        for (i, line) in lines.enumerate() {
            if i == 0 {
                for c in line.expect("Could not parse").chars() {
                    first_set.insert(c);
                }
            } else if i == 1 {
                for c in line.expect("Could not parse").chars() {
                    second_set.insert(c);
                }
            } else if i == 2 {
                for c in line.expect("Could not parse").chars() {
                    third_set.insert(c);
                }
            };
        }
        let common: HashSet<_> = first_set.intersection(&second_set).cloned().collect();
        let common: HashSet<_> = common.intersection(&third_set).cloned().collect();
        let mut priority: u32 = 0;
        for c in common {
            let c_char: char = c;
            if c_char.is_uppercase() {
                priority = priority + c_char.to_ascii_lowercase() as u32 - 70;
            } else if c_char.is_lowercase() {
                priority = priority + c_char.to_ascii_uppercase() as u32 - 64;
            }
        }
        total = total + priority;
    }
    total
}
