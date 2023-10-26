use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> i32 {
    let f = File::open("./input/data_22").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut grid: Vec<Vec<char>> = Vec::new();
    let mut steps: Vec<i32> = Vec::new();
    let mut rotate: Vec<char> = Vec::new();
    let re_num = Regex::new(r"(\d+)").unwrap();
    let re_lett = Regex::new(r"([A-Z])").unwrap();

    let mut done: bool = false;

    // Parse input and pad the grid with empty spaces
    for line in f.lines() {
        if let Ok(s) = line {
            if s == "" {
                done = true;
                continue;
            }
            if !done {
                let mut row: Vec<char> = Vec::new();
                row.push(' ');
                for c in s.chars() {
                    row.push(c);
                }
                row.push(' ');
                grid.push(row);
            } else {
                let matches_num = re_num.find_iter(&s);
                let matches_lett= re_lett.find_iter(&s);
                for step in matches_num {
                    steps.push(step.as_str().parse::<i32>().unwrap());
                }
                for lett in matches_lett {
                    rotate.push(lett.as_str().chars().nth(0).unwrap());
                }

            }
        }
    }
    grid.insert(0, vec![' '; grid[0].len()]);
    grid.push(vec![' '; grid[0].len()]);
    // for line in grid.iter() {
    //     println!("{:?}", line);
    // }
    // println!("{:?}", steps);
    // println!("{:?}", rotate);

    // Pad rows that are too short
    let max_len = grid.iter().max_by(|&v, &w| v.len().cmp(&w.len())).unwrap().len();
    for i in 0..grid.len() {
        if grid[i].len() < max_len {
            let mut pad = vec![' '; max_len - grid[i].len()];
            grid[i].append(& mut pad);
        }
    }

    let mut position: (i32, i32) = (1, grid[1].iter().position(|&v| v == '.').unwrap() as i32);
    let mut direction: (i32, i32) = (0, 1); // to the right


    for i in 0..steps.len() - 1 {
        // Take steps
        position = update_pos(position.clone(), steps[i] as u32, grid.clone(), direction);
        // Rotate
        if rotate[i] == 'L' {
            if direction == (0, 1) {
                direction = (-1, 0);
            } else if direction == (-1, 0) {
                direction = (0, -1);
            } else if direction == (0, -1) {
                direction = (1, 0);
            } else if direction == (1, 0) {
                direction = (0, 1);
            }
        } else {
            if direction == (0, 1) {
                direction = (1, 0);
            } else if direction == (1, 0) {
                direction = (0, -1);
            } else if direction == (0, -1) {
                direction = (-1, 0);
            } else if direction == (-1, 0) {
                direction = (0, 1);
            }
        }
    }
    // One more step
    position = update_pos(position.clone(), steps[steps.len() - 1] as u32, grid.clone(), direction);

    let dir_score: i32 = match direction {
        (0, 1) => 0,
        (1, 0) => 1,
        (0, -1) => 2,
        (-1, 0) => 3,
        _ => 0
    };
    dir_score + 1000 * position.0 + 4 * position.1
}

fn update_pos(mut position: (i32, i32), steps: u32, grid: Vec<Vec<char>>, direction: (i32, i32)) -> (i32, i32)
{
    'outer: for _step in 0..steps {
        if grid[(position.0 + direction.0) as usize][(position.1 + direction.1) as usize] == '#' {
            break 'outer;
        } else if grid[(position.0 + direction.0) as usize][(position.1 + direction.1) as usize] == ' ' {
            // Looping around
            if direction.1 == 1 {
                // Going right
                let new_pos = grid[position.0 as usize].iter().position(|v| *v != ' ').unwrap() as i32;
                if grid[position.0 as usize][new_pos as usize] == '#' {
                    break 'outer;
                } else {
                    position.1 = new_pos;
                }
            } else if direction.1 == -1 {
                // Going left
                let new_pos = grid[position.0 as usize].iter().rposition(|v| *v != ' ').unwrap() as i32;
                if grid[position.0 as usize][new_pos as usize] == '#' {
                    break 'outer;
                } else {
                    position.1 = new_pos;
                }
            } else if direction.0 == 1 {
                // Going down
                let new_pos = grid.iter().position(|v| v[position.1 as usize] != ' ').unwrap() as i32;
                if grid[new_pos as usize][position.1 as usize] == '#' {
                    break 'outer;
                } else {
                    position.0 = new_pos;
                }
            } else if direction.0 == -1 {
                // Going up
                let new_pos = grid.iter().rposition(|v| v[position.1 as usize] != ' ').unwrap() as i32;
                if grid[new_pos as usize][position.1 as usize] == '#' {
                    break 'outer;
                } else {
                    position.0 = new_pos;
                }
            }
        } else {
            // Make move
            position = (position.0 + direction.0, position.1 + direction.1);
        }
    }
    position
}

fn part2() -> i32 {
    let f = File::open("./input/data_22").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut grid: Vec<Vec<char>> = Vec::new();
    let mut steps: Vec<i32> = Vec::new();
    let mut rotate: Vec<char> = Vec::new();
    let re_num = Regex::new(r"(\d+)").unwrap();
    let re_lett = Regex::new(r"([A-Z])").unwrap();

    let mut done: bool = false;

    // Parse input an pad the grid with empty spaces
    for line in f.lines() {
        if let Ok(s) = line {
            // println!("{s}");
            if s == "" {
                done = true;
                continue;
            }
            if !done {
                let mut row: Vec<char> = Vec::new();
                row.push(' ');
                for c in s.chars() {
                    row.push(c);
                }
                row.push(' ');
                grid.push(row);
            } else {
                let matches_num = re_num.find_iter(&s);
                let matches_lett= re_lett.find_iter(&s);
                for step in matches_num {
                    steps.push(step.as_str().parse::<i32>().unwrap());
                }
                for lett in matches_lett {
                    rotate.push(lett.as_str().chars().nth(0).unwrap());
                }

            }
        }
    }
    grid.insert(0, vec![' '; grid[0].len()]);
    grid.push(vec![' '; grid[0].len()]);

    // Pad rows that are too short
    let max_len = grid.iter().max_by(|&v, &w| v.len().cmp(&w.len())).unwrap().len();
    for i in 0..grid.len() {
        if grid[i].len() < max_len {
            let mut pad = vec![' '; max_len - grid[i].len()];
            grid[i].append(& mut pad);
        }
    }

    let mut position: (i32, i32) = (1, grid[1].iter().position(|&v| v == '.').unwrap() as i32);
    let mut direction: (i32, i32) = (0, 1); // to the right


    for i in 0..steps.len() - 1 {
        // Take steps
        (position, direction) = update_pos_dir(position.clone(), steps[i] as u32, grid.clone(), direction.clone());
        // Rotate
        if rotate[i] == 'L' {
            if direction == (0, 1) {
                direction = (-1, 0);
            } else if direction == (-1, 0) {
                direction = (0, -1);
            } else if direction == (0, -1) {
                direction = (1, 0);
            } else if direction == (1, 0) {
                direction = (0, 1);
            }
        } else {
            if direction == (0, 1) {
                direction = (1, 0);
            } else if direction == (1, 0) {
                direction = (0, -1);
            } else if direction == (0, -1) {
                direction = (-1, 0);
            } else if direction == (-1, 0) {
                direction = (0, 1);
            }
        }
    }
    // One more step
    (position, direction) = update_pos_dir(position.clone(), steps[steps.len() - 1] as u32, grid.clone(), direction.clone());

    let dir_score: i32 = match direction {
        (0, 1) => 0,
        (1, 0) => 1,
        (0, -1) => 2,
        (-1, 0) => 3,
        _ => 0
    };
    dir_score + 1000 * position.0 + 4 * position.1
}

fn update_pos_dir(mut position: (i32, i32), steps: u32, grid: Vec<Vec<char>>, mut direction: (i32, i32)) -> ((i32, i32), (i32, i32))
{
    'outer: for _step in 0..steps {
        if grid[(position.0 + direction.0) as usize][(position.1 + direction.1) as usize] == '#' {
            break 'outer;
        } else if grid[(position.0 + direction.0) as usize][(position.1 + direction.1) as usize] == ' ' {
            // Looping around
            if direction.1 == 1 {
                // Going right
                let new_pos: (i32, i32);
                let new_dir: (i32, i32);
                if position.0 <= 50 {
                    new_pos = (101 + 50 - position.0, grid[101 + (50 - position.0) as usize].iter().rposition(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, -1);
                } else if position.0 <= 100 {
                    new_pos = (grid.iter().rposition(|v| v[(position.0 - 50 + 100) as usize] != ' ').unwrap() as i32, 100 + position.0 - 50);
                    new_dir = (-1 ,0);
                } else if position.0 <= 150 {
                    new_pos = (50 - (position.0 - 101), grid[50 - (position.0 - 100) as usize].iter().rposition(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, -1);
                } else {
                    new_pos = (grid.iter().rposition(|v| v[(50 + position.0 - 150) as usize] != ' ').unwrap() as i32, 50 + position.0 - 150);
                    new_dir = (-1 ,0);
                }
                if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
                    break 'outer;
                } else {
                    position = new_pos;
                    direction = new_dir;
                }
            } else if direction.1 == -1 {
                // Going left
                let new_pos: (i32, i32);
                let new_dir: (i32, i32);
                if position.0 <= 50 {
                    new_pos = (151 - position.0, grid[151 - position.0 as usize].iter().position(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, 1);
                } else if position.0 <= 100 {
                    new_pos = (grid.iter().position(|v| v[position.0 as usize - 50] != ' ').unwrap() as i32, position.0 - 50);
                    new_dir = (1 ,0);
                } else if position.0 <= 150 {
                    new_pos = (151 - position.0, grid[151 - position.0 as usize].iter().position(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, 1);
                } else {
                    new_pos = (grid.iter().position(|v| v[(50 + position.0 - 150) as usize] != ' ').unwrap() as i32, (50 + position.0) - 150);
                    new_dir = (1 ,0);
                }
                if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
                    break 'outer;
                } else {
                    position = new_pos;
                    direction = new_dir;
                }
            } else if direction.0 == 1 {
                // Going down
                let new_pos: (i32, i32);
                let new_dir: (i32, i32);
                if position.1 <= 50 {
                    new_pos = (grid.iter().position(|v| v[100 + position.1 as usize] != ' ').unwrap() as i32, 100 + position.1);
                    new_dir = (1 ,0);
                } else if position.1 <= 100 {
                    new_pos = (150 + position.1 - 50, grid[(150 + position.1 - 50) as usize].iter().rposition(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, -1);
                } else {
                    new_pos = (50 + position.1 - 100, grid[(50 + position.1 - 100) as usize].iter().rposition(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, -1);
                }
                if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
                    break 'outer;
                } else {
                    position = new_pos;
                    direction = new_dir;
                }
            } else if direction.0 == -1 {
                // Going up
                let new_pos: (i32, i32);
                let new_dir: (i32, i32);
                if position.1 <= 50 {
                    new_pos = (50 + position.1, grid[50 + position.1 as usize].iter().position(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, 1);
                } else if position.1 <= 100 {
                    new_pos = (150 + position.1 - 50, grid[150 + position.1 as usize - 50].iter().position(|v| *v != ' ').unwrap() as i32);
                    new_dir = (0, 1);
                } else {
                    new_pos = (grid.iter().rposition(|v| v[position.1 as usize - 100] != ' ').unwrap() as i32, position.1 - 100);
                    new_dir = (-1 ,0);
                }
                if grid[new_pos.0 as usize][new_pos.1 as usize] == '#' {
                    break 'outer;
                } else {
                    position = new_pos;
                    direction = new_dir;
                }
            }
        } else {
            // Make move
            position = (position.0 + direction.0, position.1 + direction.1);
        }
    }
    (position, direction)
}