use std::fs::File;
use std::io::{BufRead, BufReader};
use slicestring::Slice;
use std::collections::HashMap;


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let mut sum_size: u32 = 0;

    let dirs = get_dir_sizes();

    for val in dirs.values() {
        if *val < 100000 {
            sum_size += *val;
        }
    }
    sum_size
}


fn part2() -> u32 {
    let dirs = get_dir_sizes();

    let tot_size: u32 = *dirs.values().max().unwrap();
    let to_free = tot_size - 40000000;

    let candidates: Vec<u32> = dirs.values().filter(|val| val > &&to_free).cloned().collect();

    let size: u32 = *candidates.iter().min().unwrap();
    size

}


fn get_dir_sizes() -> HashMap<String, u32> {
    let f = File::open("./input/data_07").expect("Unable to open file");
    let f = BufReader::new(f);
    
    let mut dirs: HashMap<String, u32> = HashMap::new();
    dirs.insert("/".to_string(), 0);

    let mut curr: Vec<String> = Vec::new();
    for line in f.lines() {
        if let Ok(s) = line {
            if s.chars().nth(0) == Some('$') {
                if s.chars().nth(2) == Some('c') {
                    let this_dir = s.slice(5..);
                    if this_dir == ".." {
                        // Move up
                        let add_size: u32 = *dirs.get(&curr[curr.len() - 1]).unwrap();
                        curr.pop();
                        *dirs.get_mut(&curr[curr.len() - 1]).unwrap() += add_size;

                    } else {
                        // Move down
                        let par: String = curr.last().unwrap_or(&"".to_string()).to_string();
                        let abs_dir: String = par + &this_dir;
                        curr.push(abs_dir);
                    }
                } else if s.chars().nth(2) == Some('l') {
                    // Nothing
                }
            } else {
                // Output for files
                if s.slice(..3) == "dir" {
                    let new_dir = s.slice(4..);
                    let par: String = curr.last().unwrap_or(&"".to_string()).to_string();
                    let abs_dir: String = par + &new_dir;
                    dirs.insert(abs_dir, 0);
                    // it is a directory
                }
                else {
                    let size: u32 = s.split(' ').collect::<Vec<&str>>()[0].parse().unwrap();
                    let subdir = &curr[curr.len() - 1];
                    *dirs.get_mut(subdir).unwrap() += size;
                }
            }
        }
    }
    while curr.len() > 1 {
        // Go back up and add the subdirs to current dir
        let add_size: u32 = *dirs.get(&curr[curr.len() - 1]).unwrap();
        curr.pop();
        *dirs.get_mut(&curr[curr.len() - 1]).unwrap() += add_size;
    }

    dirs
}