use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;
use itertools::{self, Itertools};


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let f = File::open("./input/data_18").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut cubes: HashSet<(i32, i32, i32)> = HashSet::new();

    let mut free_edges: i32 = 0;
    
    for line in f.lines() {
        if let Ok(s) = line {
            let coords: Vec<&str> = s.split(',').collect();
            let coord_tup: (i32, i32, i32) = coords.iter().map(|v| v.parse::<i32>().unwrap()).next_tuple().unwrap();
            free_edges += 6 - 2*find_num_neighbours(coord_tup, cubes.clone());
            cubes.insert(coord_tup);
        }
    }
    free_edges as i32
}

fn part2() -> i32 {
    let f = File::open("./input/data_18").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut cubes: HashSet<(i32, i32, i32)> = HashSet::new();

    for line in f.lines() {
        if let Ok(s) = line {
            let coords: Vec<&str> = s.split(',').collect();
            let coord_tup: (i32, i32, i32) = coords.iter().map(|v| v.parse::<i32>().unwrap() + 1).next_tuple().unwrap();
            cubes.insert(coord_tup);
        }
    }

    // Do a flood fill
    // (0, 0, 0) is outside the structure, no coord greater than 20 => build box (0 - 20) x (0 - 20) x (0 - 20)
    let mut outer_edges: i32 = 0;
    let mut lava: HashSet<(i32, i32 , i32)> = HashSet::new();
    let mut queue: Vec<(i32, i32, i32)> = vec![(0, 0, 0)];
    while queue.len() > 0 {
        let cube = queue.remove(0);
        let mut possible: Vec<(i32, i32, i32)> = Vec::new();
        possible.push((cube.0, cube.1, cube.2 + 1));
        possible.push((cube.0, cube.1, cube.2 - 1));
        possible.push((cube.0, cube.1 + 1, cube.2));
        possible.push((cube.0, cube.1 - 1, cube.2));
        possible.push((cube.0 + 1, cube.1, cube.2));
        possible.push((cube.0 - 1, cube.1, cube.2));

        for c in possible.clone() {
            if !cubes.contains(&c) && c.0 <= 30 && c.0 >= 0 && c.1 <= 30 && c.1 >= 0 && c.2 <= 30 && c.2 >= 0 && !lava.contains(&c) {
                queue.push(c);
                lava.insert(c);
            }
        }
        for c in possible.clone() {
            if cubes.contains(&c) {
                outer_edges += 1;
            }
        }

    }
    outer_edges
}

fn find_num_neighbours(cube: (i32, i32, i32), cubes: HashSet<(i32, i32, i32)>) -> i32 {
    let mut possible: Vec<(i32, i32, i32)> = Vec::new();
    possible.push((cube.0, cube.1, cube.2 + 1));
    possible.push((cube.0, cube.1, cube.2 - 1));
    possible.push((cube.0, cube.1 + 1, cube.2));
    possible.push((cube.0, cube.1 - 1, cube.2));
    possible.push((cube.0 + 1, cube.1, cube.2));
    possible.push((cube.0 - 1, cube.1, cube.2));

    let mut count: i32 = 0;
    for c in possible {
        if cubes.contains(&c) {
            count += 1;
        }
    }
    count
}