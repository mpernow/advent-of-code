use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;
use std::collections::HashSet;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_14").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut occupied: HashSet<(i32, i32)> = HashSet::new();
    let mut deepest: i32 = 0;

    for line in f.lines() {
        if let Ok(s) = line {
            let path = s.split(" -> ").collect::<Vec<&str>>();
            let mut current_ind = 0;
            let current_vertex: (i32, i32) = path[current_ind].split(',').map(|s| s.parse::<i32>().unwrap()).collect_tuple().unwrap();
            occupied.insert(current_vertex);
            while current_ind < path.len() - 1 {
                let current_vertex: (i32, i32) = path[current_ind].split(',').map(|s| s.parse::<i32>().unwrap()).collect_tuple().unwrap();
                let next_vertex: (i32, i32) = path[current_ind+1].split(',').map(|s| s.parse::<i32>().unwrap()).collect_tuple().unwrap();
                let diff: (i32, i32) = (next_vertex.0 - current_vertex.0, next_vertex.1 - current_vertex.1);
                let steps: i32 = (diff.0 + diff.1).abs();
                let direction: (i32, i32) = (diff.0.signum(), diff.1.signum());
                for i in 1..(steps+1) {
                    occupied.insert((current_vertex.0 + i*direction.0, current_vertex.1 + i*direction.1));
                }
                if next_vertex.1 > deepest {
                    deepest = next_vertex.1;
                }
                current_ind += 1;
            }
        }
    }

    let mut num_sand: u32 = 0;
    'outer: loop {
        let mut sand: (i32, i32) = (500, 0);
        while !(occupied.contains(&(sand.0, sand.1 + 1))) || !(occupied.contains(&(sand.0 - 1, sand.1 + 1))) || !(occupied.contains(&(sand.0 + 1, sand.1 + 1))) {
            if !(occupied.contains(&(sand.0, sand.1 + 1))) {
                sand = (sand.0, sand.1 + 1);
            } else if !(occupied.contains(&(sand.0 - 1, sand.1 + 1))) {
                sand = (sand.0 - 1, sand.1 + 1);
            } else {
                sand = (sand.0 + 1, sand.1 + 1);
            }
            if sand.1 >= deepest {
                break 'outer;
            }
        }
        occupied.insert(sand);
        num_sand += 1;
    }
    num_sand
}

fn part2() -> u32 {
    let f = File::open("./input/data_14").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut occupied: HashSet<(i32, i32)> = HashSet::new();
    let mut deepest: i32 = 0;

    for line in f.lines() {
        if let Ok(s) = line {
            let path = s.split(" -> ").collect::<Vec<&str>>();
            let mut current_ind = 0;
            let current_vertex: (i32, i32) = path[current_ind].split(',').map(|s| s.parse::<i32>().unwrap()).collect_tuple().unwrap();
            occupied.insert(current_vertex);
            while current_ind < path.len() - 1 {
                let current_vertex: (i32, i32) = path[current_ind].split(',').map(|s| s.parse::<i32>().unwrap()).collect_tuple().unwrap();
                let next_vertex: (i32, i32) = path[current_ind+1].split(',').map(|s| s.parse::<i32>().unwrap()).collect_tuple().unwrap();
                let diff: (i32, i32) = (next_vertex.0 - current_vertex.0, next_vertex.1 - current_vertex.1);
                let steps: i32 = (diff.0 + diff.1).abs();
                let direction: (i32, i32) = (diff.0.signum(), diff.1.signum());
                for i in 1..(steps+1) {
                    occupied.insert((current_vertex.0 + i*direction.0, current_vertex.1 + i*direction.1));
                }
                if next_vertex.1 > deepest {
                    deepest = next_vertex.1;
                }
                current_ind += 1;
            }
        }
    }

    let mut num_sand: u32 = 0;
    loop {
        let mut sand: (i32, i32) = (500, 0);
        while (!(occupied.contains(&(sand.0, sand.1 + 1))) || !(occupied.contains(&(sand.0 - 1, sand.1 + 1))) || !(occupied.contains(&(sand.0 + 1, sand.1 + 1)))) && (sand.1 < deepest + 1) {
            if !(occupied.contains(&(sand.0, sand.1 + 1))) {
                sand = (sand.0, sand.1 + 1);
            } else if !(occupied.contains(&(sand.0 - 1, sand.1 + 1))) {
                sand = (sand.0 - 1, sand.1 + 1);
            } else {
                sand = (sand.0 + 1, sand.1 + 1);
            }
        }
        occupied.insert(sand);
        num_sand += 1;
        if sand == (500, 0) {
            break;
        }
    }
    num_sand
}
