use std::fs::File;
use std::io::{BufRead, BufReader};


fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let tree_heights = tree_heights();

    let rows: usize = tree_heights.len();
    let cols: usize = tree_heights[0].len();
    let mut visible: Vec<Vec<u32>> = Vec::new();
    for _ in 0..rows{
        let row = vec![0; cols];
        visible.push(row);
    }

    for r in 0..rows {
        // Check visible trees from left
        let mut highest: i32 = -1;
        for c in 0..cols {
            if tree_heights[r][c] as i32 > highest {
                highest = tree_heights[r][c] as i32;
                visible[r][c] = 1;
            }
        }
    }
    for r in 0..rows {
        // Check visible trees from right 
        let mut highest: i32 = -1;
        for c in (0..cols).rev() {
            if tree_heights[r][c] as i32 > highest {
                highest = tree_heights[r][c] as i32;
                visible[r][c] = 1;
            }
        }
    }
    for c in 0..cols {
        // Check visible trees from above 
        let mut highest: i32 = -1;
        for r in 0..rows {
            if tree_heights[r][c] as i32 > highest {
                highest = tree_heights[r][c] as i32;
                visible[r][c] = 1;
            }
        }
    }
    for c in 0..cols {
        // Check visible trees from below 
        let mut highest: i32 = -1;
        for r in (0..rows).rev() {
            if tree_heights[r][c] as i32 > highest {
                highest = tree_heights[r][c] as i32;
                visible[r][c] = 1;
            }
        }
    }
    visible.iter().map(|x| -> u32 { x.iter().sum() }).sum()
}

fn part2() -> u32 {
    let tree_heights = tree_heights();

    let rows: usize = tree_heights.len();
    let cols: usize = tree_heights[0].len();

    let mut best: u32 = 0;
    for r in 1..(rows-1) {
        for c in 1..(cols-1) {
            let this_height = tree_heights[r][c];
            let mut up = 1;
            let mut down = 1;
            let mut left = 1;
            let mut right = 1;
            // Go up
            let mut row_idx = r-1;
            while (row_idx > 0) & (tree_heights[row_idx][c] < this_height) {
                row_idx -= 1;
                up += 1;
            } 
            // Go down 
            let mut row_idx = r+1;
            while (row_idx < rows-1) & (tree_heights[row_idx][c] < this_height) {
                row_idx += 1;
                down += 1;
            } 
            // Go left 
            let mut col_idx = c-1;
            while (col_idx > 0) & (tree_heights[r][col_idx] < this_height) {
                col_idx -= 1;
                left += 1;
            } 
            // Go right 
            let mut col_idx = c+1;
            while (col_idx < cols-1) & (tree_heights[r][col_idx] < this_height) {
                col_idx += 1;
                right += 1;
            } 
            if up*down*left*right > best {
                best = up*down*left*right;
            }
        }
    }
    best
}

fn tree_heights() -> Vec<Vec<u32>> {
    let f = File::open("./input/data_08").expect("Unable to open file");
    let f = BufReader::new(f);
    
    let mut trees: Vec<Vec<u32>> = Vec::new();
    for line in f.lines() {
        if let Ok(s) = line {
            let tree_row: Vec<u32> = s.chars().map(|x| x.to_digit(10).unwrap()).collect();
            trees.push(tree_row);
        }
    }
    trees
}