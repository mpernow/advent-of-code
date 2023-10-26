use std::fs::File;
use std::io::{BufRead, BufReader};
use slicestring::Slice;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_11").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut items: Vec<Vec<u32>> = Vec::new();
    let operations: Vec<&dyn Fn(u32) -> u32> = vec![&times7, &plus5, &square, &plus4, &times17, &plus7, &plus6, &plus3];
    let mut divisibility: Vec<u32> = Vec::new();
    let mut if_true: Vec<u32> = Vec::new();
    let mut if_false: Vec<u32> = Vec::new();

    for line in f.lines() {
        if let Ok(s) = line {
            if s.slice(2..3) == "S" {
                // Starting items
                let item_str: String = s.slice(18..);
                let item_vec: Vec<u32> = item_str.split(',').map(|s| s.trim())
                                                 .filter(|s| !s.is_empty())
                                                 .map(|s| s.parse().unwrap())
                                                 .collect();
                items.push(item_vec);
            } else if s.slice(2..3) == "T" {
                // Test
                divisibility.push(s.slice(21..).parse::<u32>().unwrap());
            } else if s.slice(7..11) == "true" {
                // if true
                if_true.push(s.slice(29..).parse::<u32>().unwrap());
            } else if s.slice(7..12) == "false" {
                 // if false
                if_false.push(s.slice(30..).parse::<u32>().unwrap());
            }
        }
    }

    let num_monkeys = items.len();
    let mut num_inspections: Vec<u32> = vec![0; num_monkeys];
    for _i in 0..20 {
        // Run operation
        for m in 0..num_monkeys {
            let mut num_items = items[m].len();
            while num_items > 0 {
                num_inspections[m] += 1;
                let item = items[m].remove(0);
                num_items = items[m].len();
                let new_val = operations[m](item) / 3;
                let outcome = new_val % divisibility[m] == 0;
                if outcome == true {
                    let destination = if_true[m] as usize;
                    items[destination].push(new_val);
                } else {
                    let destination = if_false[m] as usize;
                    items[destination].push(new_val);
                }
            }
        }
    }
    num_inspections.sort();
    num_inspections[num_inspections.len() - 1] * num_inspections[num_inspections.len() - 2]
}

// Hard coded, ugly!
fn times7(x: u32) -> u32 {
    x * 7
}

fn times17(x: u32) -> u32 {
    x * 17
}

fn plus5(x: u32) -> u32 {
    x + 5
}

fn plus4(x: u32) -> u32 {
    x + 4
}

fn plus7(x: u32) -> u32 {
    x + 7
}

fn plus6(x: u32) -> u32 {
    x + 6
}
fn plus3(x: u32) -> u32 {
    x + 3
 }

fn square(x: u32) -> u32 {
    x * x
}

fn part2() -> u64 {
    let f = File::open("./input/data_11").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut items: Vec<Vec<u64>> = Vec::new();
    let operations: Vec<&dyn Fn(&u64) -> u64> = vec![&times7big, &plus5big, &squarebig, &plus4big, &times17big, &plus7big, &plus6big, &plus3big];
    let mut divisibility: Vec<u64> = Vec::new();
    let mut if_true: Vec<u32> = Vec::new();
    let mut if_false: Vec<u32> = Vec::new();

    for line in f.lines() {
        if let Ok(s) = line {
            if s.slice(2..3) == "S" {
                // Starting items
                let item_str: String = s.slice(18..);
                let item_vec: Vec<u64> = item_str.split(',').map(|s| s.trim())
                                                 .filter(|s| !s.is_empty())
                                                 .map(|s| s.parse().unwrap())
                                                 .collect();
                items.push(item_vec);
            } else if s.slice(2..3) == "T" {
                // Test
                divisibility.push(s.slice(21..).parse::<u64>().unwrap());
            } else if s.slice(7..11) == "true" {
                // if true
                if_true.push(s.slice(29..).parse::<u32>().unwrap());
            } else if s.slice(7..12) == "false" {
                 // if false
                if_false.push(s.slice(30..).parse::<u32>().unwrap());
            }
        }
    }

    let lcm = divisibility.iter().copied().reduce(|a, b| a*b).unwrap();
    let num_monkeys = items.len();
    let mut num_inspections: Vec<u32> = vec![0; num_monkeys];
    for _i in 0..10000 {
        // Run operation
        for m in 0..num_monkeys {
            let mut num_items = items[m].len();
            while num_items > 0 {
                num_inspections[m] += 1;
                let item = items[m].remove(0);
                num_items = items[m].len();
                let mut new_val = operations[m](&item);
                new_val %= lcm;
                let outcome = bigmodulooutcome(&new_val, &(divisibility[m]));
                if outcome == true {
                    let destination = if_true[m] as usize;
                    items[destination].push(new_val);
                } else {
                    let destination = if_false[m] as usize;
                    items[destination].push(new_val);
                }
            }
        }
    }
    num_inspections.sort();
    num_inspections[num_inspections.len() - 1] as u64 * num_inspections[num_inspections.len() - 2] as u64
    // 0
}

// Hard coded, ugly!
fn times7big(x: &u64) -> u64 {
    x * 7
}

fn times17big(x: &u64) -> u64 {
    x * 17
}

fn plus5big(x: &u64 ) -> u64 {
    x + 5
}

fn plus4big(x: &u64 ) -> u64 {
    x + 4
}

fn plus7big(x: &u64 ) -> u64 {
    x + 7
}

fn plus6big(x: &u64 ) -> u64 {
    x + 6
}
fn plus3big(x: &u64 ) -> u64 {
    x + 3
 }

fn squarebig(x: &u64) -> u64 {
    x * x
}

fn bigmodulooutcome(x: &u64, m: &u64) -> bool {
    x % m == 0
}