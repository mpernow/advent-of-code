use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashMap;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_17").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut wind: String = String::new();

    for line in f.lines() {
        if let Ok(s) = line {
            wind = s;
        }
    }
    // println!("{wind}");
    
    let mut chamber: Vec<Vec<bool>> = vec![vec![false; 7]; 4];
    // println!("{:?}",chamber);
    
    // Shapes of the blocks, given as starting positions (x, y), assuming the highest block is located at y = 4
    let horizontal: Vec<(i32, i32)> = vec![(2, 0), (3, 0), (4, 0), (5, 0)];
    let plus: Vec<(i32, i32)> = vec![(3, -2), (2, -1), (3, -1), (4, -1), (3, 0)];
    let angle: Vec<(i32, i32)> = vec![(4, -2), (4, -1), (2, 0), (3, 0), (4, 0)];
    let vertical: Vec<(i32, i32)> = vec![(2, 0), (2, -1), (2, -2), (2, -3)];
    let square: Vec<(i32, i32)> = vec![(2, -1), (3, -1), (2, 0), (3, 0)];

    let block_order: Vec<Vec<(i32, i32)>> = vec![horizontal, plus, angle, vertical, square];

    let mut wind_idx: u32 = 0;
    let mut height_counter: u32 = 0;
    let mut new_height: u32;

    let num_rocks = 2022;
    // let num_rocks = 4;
    for block_idx in 0..num_rocks {
        (chamber, wind_idx, new_height) = place_block(chamber, block_order[block_idx % 5].clone(), wind_idx, wind.clone());
        height_counter += new_height;
    }

    height_counter 
}

fn part2() -> u64 {
    let f = File::open("./input/data_17").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut wind: String = String::new();

    for line in f.lines() {
        if let Ok(s) = line {
            wind = s;
        }
    }
    // println!("{wind}");
    
    let mut chamber: Vec<Vec<bool>> = vec![vec![false; 7]; 4];
    
    // Shapes of the blocks, given as starting positions (x, y), assuming the highest block is located at y = 4
    let horizontal: Vec<(i32, i32)> = vec![(2, 0), (3, 0), (4, 0), (5, 0)];
    let plus: Vec<(i32, i32)> = vec![(3, -2), (2, -1), (3, -1), (4, -1), (3, 0)];
    let angle: Vec<(i32, i32)> = vec![(4, -2), (4, -1), (2, 0), (3, 0), (4, 0)];
    let vertical: Vec<(i32, i32)> = vec![(2, 0), (2, -1), (2, -2), (2, -3)];
    let square: Vec<(i32, i32)> = vec![(2, -1), (3, -1), (2, 0), (3, 0)];

    let block_order: Vec<Vec<(i32, i32)>> = vec![horizontal, plus, angle, vertical, square];

    let mut wind_idx: u32 = 0;

    // (cave top, wind_idx) -> (block_idx, height)
    let mut checkpoints: HashMap<(Vec<Vec<bool>>, u32), (u32, u64)> = HashMap::new();
    let mut height: u64 = 0;
    let mut new_height: u32;

    let num_rocks = 1000000000000;
    let mut block_idx = 0;
    while block_idx < num_rocks {
        (chamber, wind_idx, new_height) = place_block(chamber, block_order[block_idx % 5].clone(), wind_idx, wind.clone());
        block_idx += 1;
        height += new_height as u64;
        if block_idx % 5 == 0 {
            if let Some((prev_idx, prev_height)) = checkpoints.insert((top_layers(chamber.clone()), wind_idx), (block_idx as u32, height)) {
                // Already contains the state

                let height_diff = height - prev_height;
                let num_iterations = block_idx as u32 - prev_idx;

                let num_repetitions = (num_rocks as u64 - block_idx as u64) / num_iterations as u64;
                block_idx += (num_iterations as u64 * num_repetitions as u64) as usize;
                height += height_diff * num_repetitions as u64;
                checkpoints.clear();
            }
        }
    }
    height
}

fn top_layers(chamber: Vec<Vec<bool>>) -> Vec<Vec<bool>> {
    if chamber.len() >= 7 {
        return chamber.clone()[3..7].to_vec();
    } else {
        return chamber.clone()[2..].to_vec();
    }
}

fn place_block(mut chamber: Vec<Vec<bool>>, mut block: Vec<(i32, i32)>, mut wind_idx: u32, wind: String) -> (Vec<Vec<bool>>, u32, u32) {
    // Simulate block falling. Return new chamber state and wind index
    let mut at_rest = false;
    while !at_rest {
        // println!("{:?}", block);
        // Move left/right if possible
        let wind_direction = if wind.chars().nth(wind_idx as usize).unwrap() == '<' { -1 } else { 1 };
        if (wind_direction == -1) && (block.clone().iter().map(|x| x.0).min_by(|a, b| a.partial_cmp(b).unwrap()).unwrap() > 0) 
                                  && block.iter().all(|v| !(chamber[(v.1).max(0) as usize][(v.0 - 1).max(0) as usize])) {
            // Move left
            block = block.iter().map(|v| (v.0 - 1, v.1)).collect::<Vec<(i32, i32)>>();
        } else if (wind_direction == 1) && (block.iter().map(|x| x.0).max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap() <= (chamber[0].len() - 2) as i32)
                                        && block.iter().all(|v| !(chamber[(v.1).max(0) as usize][(v.0 + 1) as usize])) {
            // Move right
            block = block.iter().map(|v| (v.0 + 1, v.1)).collect::<Vec<(i32, i32)>>();
        }
        // Increment the wind index
        wind_idx = (wind_idx + 1) % wind.len() as u32;

        // Move down if possible, else come to rest
        // println!("{:?}", block);
        let mut move_down: bool = block.iter().map(|v| v.1).max_by(|a, b| a.partial_cmp(b).unwrap()).unwrap() < (chamber.len() - 1) as i32;
        if move_down {
            move_down = move_down && block.iter().all(|v| !(chamber[(v.1 + 1).max(0) as usize][v.0 as usize]));
        }
        if move_down {
            block = block.iter().map(|v| (v.0, v.1 + 1)).collect::<Vec<(i32, i32)>>();
        } else {
            // Cannot move down. Set coordinates to true in chamber
            for v in block.clone() {
                chamber[v.1 as usize][v.0 as usize] = true;
            }
            at_rest = true;
        }
    }

    // Add aditional lines onto chamber if needed
    let mut line_idx = 0;
    for (i, line) in chamber.iter().enumerate() {
        if line.iter().any(|v| *v) {
            line_idx = i;
            break;

        }
    }
    let mut new_height = 0;
    for _i in 0..(4 - line_idx) {
        chamber.insert(0, vec![false; chamber[0].len()]);
        new_height += 1;
    }
    (chamber, wind_idx, new_height)
}