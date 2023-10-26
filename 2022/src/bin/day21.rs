use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

use itertools::Itertools;


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i64 {
    let f = File::open("./input/data_21").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut known: HashMap<String, i64> = HashMap::new();
    let mut unknown: HashMap<String, Vec<String>> = HashMap::new();

    for line in f.lines() {
        if let Ok(s) = line {
            let split_str = s.split(" ").map(String::from).collect_vec();
            let name = split_str.clone()[0].to_string();
            if split_str.clone().len() == 2 {
                known.insert(name[..name.len() - 1].to_string(), split_str.clone()[1].parse::<i64>().unwrap());
            } else {
                unknown.insert(name[..name.len() - 1].to_string(), split_str[1..].to_vec());
            }
        }
    }

    while unknown.contains_key("root") {
        let unknown_monkeys = unknown.clone();
        for monkey in unknown_monkeys {
            if known.contains_key(&monkey.1[0]) && known.contains_key(&monkey.1[2]) {
                let operation = &monkey.1[1];
                if operation == "+" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] + known[&monkey.1[2]]);
                }
                if operation == "-" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] - known[&monkey.1[2]]);
                }
                if operation == "*" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] * known[&monkey.1[2]]);
                }
                if operation == "/" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] / known[&monkey.1[2]]);
                }
                unknown.remove(&monkey.0);
            }
        }
    }

    known["root"]
}

fn part2() -> i64 {
    let f = File::open("./input/data_21").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut known: HashMap<String, i64> = HashMap::new();
    let mut unknown: HashMap<String, Vec<String>> = HashMap::new();

    for line in f.lines() {
        if let Ok(s) = line {
            let split_str = s.split(" ").map(String::from).collect_vec();
            let name = split_str.clone()[0].to_string();
            if split_str.clone().len() == 2 {
                known.insert(name[..name.len() - 1].to_string(), split_str.clone()[1].parse::<i64>().unwrap());
            } else {
                unknown.insert(name[..name.len() - 1].to_string(), split_str[1..].to_vec());
            }
        }
    }
    let left = unknown["root"][0].clone();
    let right = unknown["root"][2].clone();
    unknown.remove("root");    
    known.remove("humn");

    let mut low: i64 = 0;
    let mut high: i64 = 10000000000000000;
    let mut humn: i64;

    loop {
        humn = (high + low) / 2;
        let left_right = get_left_right(unknown.clone(), known.clone(), left.clone(), right.clone(), humn);
        if left_right.0 == left_right.1 {
            break;
        }
        if left_right.0 > left_right.1 {
            // If left is too large, need to raise humn
            low = humn;
        } else {
            // If left is too small, need to lower humn
            high = humn;
        }
    }

    humn
}

fn get_left_right(mut unknown: HashMap<String, Vec<String>>, mut known: HashMap<String, i64>, left: String, right: String, humn: i64) -> (i64, i64) {
    // println!("{left}, {right}");
    known.insert("humn".to_string(), humn);
    while (unknown.contains_key(&left)) || (unknown.contains_key(&right)) {
        // println!(" ");
        // println!("{:?}", unknown);
        // println!("{:?}", known);
        let unknown_monkeys = unknown.clone();
        for monkey in unknown_monkeys {
            if known.contains_key(&monkey.1[0]) && known.contains_key(&monkey.1[2]) {
                let operation = &monkey.1[1];
                if operation == "+" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] + known[&monkey.1[2]]);
                }
                if operation == "-" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] - known[&monkey.1[2]]);
                }
                if operation == "*" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] * known[&monkey.1[2]]);
                }
                if operation == "/" {
                    known.insert(monkey.0.to_string(), known[&monkey.1[0]] / known[&monkey.1[2]]);
                }
                unknown.remove(&monkey.0);
            }
        }
    }
    // println!("{}", known[&left]);
    // println!("{}", known[&right]);
    (known[&left], known[&right])
}