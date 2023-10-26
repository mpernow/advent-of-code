use std::fs::File;
use std::io::{BufRead, BufReader};

// Note: incomplete since did not keep track of cycling through directions!

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let f = File::open("./input/data_23").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut elves: Vec<(i32, i32)> = Vec::new();

    // Import grid with padding of 10 since that is the largest number of steps they can take
    for (r, line) in f.lines().enumerate() {
        if let Ok(s) = line {
            for (c, val) in s.chars().enumerate() {
                if val == '#' {
                    elves.push((r as i32, c as i32));
                }
            }
        }
    }
    

    let num_iter = 10;
    for round in 0..num_iter {
        elves = update_pos(elves.clone(), round);
    }
    (elves.iter().max_by_key(|p| p.0).unwrap().0 - elves.iter().min_by_key(|p| p.0).unwrap().0 + 1) * (elves.iter().max_by_key(|p| p.1).unwrap().1 - elves.iter().min_by_key(|p| p.1).unwrap().1 + 1) - elves.len() as i32
}

fn part2() -> i32 {
    let f = File::open("./input/data_23").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut elves: Vec<(i32, i32)> = Vec::new();

    // Import grid with padding of 10 since that is the largest number of steps they can take
    for (r, line) in f.lines().enumerate() {
        if let Ok(s) = line {
            for (c, val) in s.chars().enumerate() {
                if val == '#' {
                    elves.push((r as i32, c as i32));
                }
            }
        }
    }
    

    let mut stopped = false;
    let mut round = 0;
    while stopped == false {
        let new_elves = update_pos(elves.clone(), round);
        stopped = elves == new_elves;
        elves = new_elves;
        round += 1;
    }
    round
}

fn update_pos(elves: Vec<(i32, i32)>, round: i32) -> Vec<(i32, i32)> {
    let mut new_elves: Vec<(i32, i32)> = Vec::new();
    for elf in &elves {
        // Check if neighbouring tiles empty, then continue
        let neighbouring: Vec<(i32, i32)> = vec![(elf.0, elf.1+1), (elf.0, elf.1-1), (elf.0-1, elf.1-1), (elf.0-1, elf.1), (elf.0-1, elf.1+1), (elf.0+1, elf.1-1), (elf.0+1, elf.1), (elf.0+1, elf.1+1)];
        let all_free = neighbouring.iter().all(|n| !elves.clone().contains(&n));
        if all_free {
            new_elves.push((elf.0, elf.1));
            continue;
        }
        // Else check if can move up, down, west, east (i.e. three tiles empty)

        let above: Vec<(i32, i32)> = vec![(elf.0-1, elf.1-1), (elf.0-1, elf.1), (elf.0-1, elf.1+1)];
        let above_free = above.iter().all(|n| !elves.clone().contains(&n));

        let below: Vec<(i32, i32)> = vec![(elf.0+1, elf.1-1), (elf.0+1, elf.1), (elf.0+1, elf.1+1)];
        let below_free = below.iter().all(|n| !elves.clone().contains(&n));

        let left: Vec<(i32, i32)> = vec![(elf.0+1, elf.1-1), (elf.0, elf.1-1), (elf.0-1, elf.1-1)];
        let left_free = left.iter().all(|n| !elves.clone().contains(&n));

        let right: Vec<(i32, i32)> = vec![(elf.0+1, elf.1+1), (elf.0, elf.1+1), (elf.0-1, elf.1+1)];
        let right_free = right.iter().all(|n| !elves.clone().contains(&n));

        let allowed_directions : Vec<bool> = vec![above_free, below_free, left_free, right_free];
        if allowed_directions.iter().all(|&dir| dir == false) {
            // Stay put
            new_elves.push((elf.0, elf.1));
            continue;
        }

        // Which direction to choose: 0 - up, 1 - down, 2 - left, 3 - right
        let mut to_move = round % 4;
        while allowed_directions[to_move as usize] == false {
            to_move = (to_move + 1) % 4;
        }
        if to_move == 0 {
            new_elves.push((elf.0-1, elf.1));
        } else if to_move == 1 {
            new_elves.push((elf.0+1, elf.1));
        } else if to_move == 2 {
            new_elves.push((elf.0, elf.1-1));
        } else if to_move == 3 {
            new_elves.push((elf.0, elf.1+1));
        }
    }
    // Loop through each proposition, check that there are no duplicates. If there are, set the new position to a previous 
    for i in 0..new_elves.len() {
        let occurrences = new_elves.clone().iter().enumerate().filter(|(_, &r)| r == new_elves[i]).map(|(index, _)| index).collect::<Vec<_>>();
        if occurrences.len() > 1 {
            for idx in occurrences {
                new_elves[idx] = elves[idx].clone();
            }
        }
    }
    new_elves
}