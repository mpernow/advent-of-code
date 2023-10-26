use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> String{
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut num_stacks: u32 = 0;
    let f = File::open("./input/data_05").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for (i, line) in f.lines().enumerate() {
        if let Ok(s) = line {
            if i == 0 {
                num_stacks = (s.len() as u32 + 1)/4;
                for _n in 0..num_stacks {
                    stacks.push(Vec::<char>::new());
                }
            }
            
            let first_char = match s.trim_start().chars().nth(0) {
                Some(value) => value,
                None => ' '
            };
            if first_char == '[' {
                // Add to stacks
                for n in 0..num_stacks {
                    let c = s.chars().nth(4*n as usize + 1 as usize).unwrap();
                    if c != ' ' {
                        stacks[n as usize].push(c);
                    }
                }
            } else if first_char == 'm' {
                // Move
                let instruction = s.split(" ").collect::<Vec<_>>();
                let num_move = instruction[1].parse::<i32>().unwrap();
                let origin: usize = (instruction[3].parse::<i32>().unwrap() - 1).try_into().unwrap();
                let destination: usize = (instruction[5].parse::<i32>().unwrap() - 1).try_into().unwrap();
                for _n in 0..num_move {
                    let value = stacks[origin].remove(0);
                    stacks[destination].insert(0, value);
                }
            }
        }
    }
    let mut tops: String = "".to_string();
    for stack in stacks {
        tops = tops + &stack[0].to_string(); 
    }
    tops
}

fn part2() -> String{
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut num_stacks: u32 = 0;
    let f = File::open("./input/data_05").expect("Unable to open file");
    let f = BufReader::new(f);
    
    for (i, line) in f.lines().enumerate() {
        if let Ok(s) = line {
            if i == 0 {
                num_stacks = (s.len() as u32 + 1)/4;
                for _n in 0..num_stacks {
                    stacks.push(Vec::<char>::new());
                }
            }
            
            let first_char = match s.trim_start().chars().nth(0) {
                Some(value) => value,
                None => ' '
            };
            if first_char == '[' {
                // Add to stacks
                for n in 0..num_stacks {
                    let c = s.chars().nth(4*n as usize + 1 as usize).unwrap();
                    if c != ' ' {
                        stacks[n as usize].push(c);
                    }
                }
            } else if first_char == 'm' {
                // Move
                let instruction = s.split(" ").collect::<Vec<_>>();
                let num_move = instruction[1].parse::<i32>().unwrap() as usize;
                let origin: usize = (instruction[3].parse::<i32>().unwrap() - 1).try_into().unwrap();
                let destination: usize = (instruction[5].parse::<i32>().unwrap() - 1).try_into().unwrap();
                
                let values: Vec<char> = stacks[origin].drain(0..num_move).collect();
                stacks[destination].splice(0..0, values.iter().cloned());
            }
        }
    }
    let mut tops: String = "".to_string();
    for stack in stacks {
        tops = tops + &stack[0].to_string(); 
    }
    tops
}
