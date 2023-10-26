use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_01").expect("Unable to open file");
    let f = BufReader::new(f);
    
    let mut highest = 0;
    let mut total = 0;
    
    for line in f.lines() {
        if let Ok(s) = line {
            if s == "" {
                if total > highest{
                    highest = total;
                }        
                total = 0;
            } else {
                let n: u32 = s.parse().unwrap();
                total = total + n;
            }
        }
    }
    highest
}

fn part2() -> u32 {
    let f = File::open("./input/data_01").expect("Unable to open file");
    let f = BufReader::new(f);
    
    let mut first = 0;
    let mut second= 0;
    let mut third = 0;
    let mut total = 0;
    
    for line in f.lines() {
        if let Ok(s) = line {
            if s == "" {
                if total > first{
                    third = second;
                    second = first;
                    first = total;
                } else if total > second{
                    third = second;
                    second = total;
                } else if total > third {
                    third = total;
                }
                total = 0;
            } else {
                let n: u32 = s.parse().unwrap();
                total = total + n;
            }
        }
    }
    if total > first{
        third = second;
        second = first;
        first = total;
    } else if total > second{
        third = second;
        second = total;
    } else if total > third {
        third = total;
    }
   first + second + third 
}