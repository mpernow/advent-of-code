use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let mut num_overlaps: u32 = 0;
    let f = File::open("./input/data_04").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            let clean_vec: Vec<&str> = s.split(',').collect();
            let first_range: Vec<&str> = clean_vec[0].split('-').collect();
            let second_range: Vec<&str> = clean_vec[1].split('-').collect();
            if ((first_range[0].parse::<u32>().unwrap() <= second_range[0].parse::<u32>().unwrap()) & (first_range[1].parse::<u32>().unwrap() >= second_range[1].parse::<u32>().unwrap())) |
                ((first_range[0].parse::<u32>().unwrap() >= second_range[0].parse::<u32>().unwrap()) & (first_range[1].parse::<u32>().unwrap() <= second_range[1].parse::<u32>().unwrap())) {
                num_overlaps = num_overlaps + 1;
            }
        }
    }
   num_overlaps 
}

fn part2() -> u32 {
    let mut num_overlaps: u32 = 0;
    let f = File::open("./input/data_04").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for line in f.lines() {
        if let Ok(s) = line {
            let clean_vec: Vec<&str> = s.split(',').collect();
            let first_range: Vec<&str> = clean_vec[0].split('-').collect();
            let second_range: Vec<&str> = clean_vec[1].split('-').collect();
            if (first_range[0].parse::<u32>().unwrap() <= second_range[1].parse::<u32>().unwrap()) & (second_range[0].parse::<u32>().unwrap() <= first_range[1].parse::<u32>().unwrap()) {
                num_overlaps = num_overlaps + 1;
            }
        }
    }
   num_overlaps 
}