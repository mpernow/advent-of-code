use std::fs::File;
use std::io::{BufRead, BufReader};


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i64 {
    let f = File::open("./input/data_20").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut numbers: Vec<i64> = Vec::new();
    
    for line in f.lines() {
        if let Ok(s) = line {
            numbers.push(s.parse::<i64>().unwrap());
        }
    }
    let mut indices: Vec<usize> = (0..numbers.len()).collect::<Vec<usize>>();

    for i in 0..indices.len() {
        let idx = indices[i];
        let number = numbers.remove(idx);
        let mut new_idx = (((idx as i64 + number) % numbers.len() as i64) + numbers.len() as i64) % numbers.len() as i64;
        if new_idx == 0 {
            // Wrap around to end if it is 0
            new_idx = numbers.len() as i64;
        }
        numbers.insert(new_idx as usize, number);

        // Also modify the indices if the number was moved to the right
        for ii in 0..indices.len() {
            if ii > i {
                if indices[ii] <= new_idx as usize {
                    indices[ii] -= 1;
                }
            }
        }
    }
    let zero_idx = numbers.iter().position(|&r| r == 0).unwrap();
    numbers[(zero_idx + 1000) % numbers.len()] + numbers[(zero_idx + 2000) % numbers.len()] + numbers[(zero_idx + 3000) % numbers.len()]
}

fn part2() -> i64 {
    let f = File::open("./input/data_20").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut numbers: Vec<i64> = Vec::new();
    let key: i64 = 811589153;
    
    for line in f.lines() {
        if let Ok(s) = line {
            numbers.push(s.parse::<i64>().unwrap() * key);
        }
    }
    let mut indices: Vec<usize> = (0..numbers.len()).collect::<Vec<usize>>();

    let num_reorderings = 10;
    for _n in 0..num_reorderings {
        for i in 0..indices.len() {
            let idx = indices[i];
            let number = numbers.remove(idx);
            let mut new_idx = (((idx as i64 + number) % numbers.len() as i64) + numbers.len() as i64) % numbers.len() as i64;
            if (new_idx == 0) && (idx != 0) {
                // Wrap around to end if it is 0
                new_idx = numbers.len() as i64;
            }
            numbers.insert(new_idx as usize, number);

            // Also modify the indices
            for ii in 0..indices.len() {
                if new_idx > idx as i64{
                    // Moved right
                    if (indices[ii] > idx) && (indices[ii] <= new_idx as usize) {
                        indices[ii] -= 1;
                    }
                } else if new_idx < idx as i64{
                    // Moved left
                    if (indices[ii] >= new_idx as usize) && (indices[ii] < idx) {
                        indices[ii] += 1;
                    }
                }
            }
            indices[i] = new_idx as usize;
        }
        // println!(" ");
        // println!("{:?}", numbers);
        // println!("{:?}", indices);
    }
    let zero_idx = numbers.iter().position(|&r| r == 0).unwrap();
    numbers[(zero_idx + 1000) % numbers.len()] + numbers[(zero_idx + 2000) % numbers.len()] + numbers[(zero_idx + 3000) % numbers.len()]
}