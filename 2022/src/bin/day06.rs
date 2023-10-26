use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use slicestring::Slice;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let mut start: usize = 0;
    let mut num_unique: u32 = 0;
    let f = File::open("./input/data_06").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            while num_unique < 4{
                let char_set: HashSet<char> = HashSet::from_iter(s.slice(start..start+4).chars());
                num_unique = char_set.len() as u32;
                start = start+ 1;
            }
        }
    }
   start as u32 + 3
}

fn part2() -> u32 {
    let mut start: usize = 0;
    let mut num_unique: u32 = 0;
    let f = File::open("./input/data_06").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            while num_unique < 14 {
                let char_set: HashSet<char> = HashSet::from_iter(s.slice(start..start+14).chars());
                num_unique = char_set.len() as u32;
                start = start+ 1;
            }
        }
    }
   start as u32 + 13
}