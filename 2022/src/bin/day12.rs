use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_12").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut heightmap: Vec<Vec<u32>> = Vec::new();
    let start = (20, 0);
    let end = (20, 148);
    // let start = (0, 0);
    // let end = (2, 5);

    for line in f.lines() {
        if let Ok(s) = line {
            heightmap.push(s.chars().map(|c| c as u32).collect());
        }
    }
    heightmap[start.0][start.1] = 'a' as u32;
    heightmap[end.0][end.1] = 'z' as u32;

    // let l = depth_first_search(heightmap, visited.clone(), start, end, 0);
    let l = breadth_first_search(heightmap, start, end);
    l
}

fn part2() -> u32 {
    let f = File::open("./input/data_12").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut heightmap: Vec<Vec<u32>> = Vec::new();
    let mut starts: Vec<(usize, usize)> = Vec::new();
    let mut end: (usize, usize) = (0, 0);

    for line in f.lines() {
        if let Ok(s) = line {
            heightmap.push(s.chars().map(|c| c as u32).collect());
        }
    }
    for r in 0..heightmap.len() {
        for c in 0..heightmap[0].len() {
            if heightmap[r][c] == 'a' as u32 {
                starts.push((r, c));
            } else if heightmap[r][c] == 'S' as u32 {
                starts.push((r, c));
                heightmap[r][c] = 'a' as u32;
            } else if heightmap[r][c] == 'E' as u32 {
                end = (r, c);
                heightmap[r][c] = 'z' as u32;
            }
        }
    }

    let mut lengths: Vec<u32> = Vec::new();
    for start in starts {
        lengths.push(breadth_first_search(heightmap.clone(), start, end))
    }
    lengths.sort();
    lengths[0]
}

fn breadth_first_search(heightmap: Vec<Vec<u32>>, start: (usize, usize), goal: (usize, usize)) -> u32 {
    let mut to_visit: Vec<((usize, usize), u32)> = Vec::new();
    let mut shortest = u32::MAX / 2;
    let mut shortest_visited: HashMap<(usize, usize), u32> = HashMap::new();
    
    to_visit.push((start, 0));

    while to_visit.len() > 0 {
        let next = to_visit.remove(0);
        let next_position = next.0;
        let mut steps = next.1;
        shortest_visited.insert(next_position, steps);
        if (next_position.0 == goal.0) & (next_position.1 == goal.1) {
            shortest = shortest.min(steps);
        }
        steps += 1;

        if next_position.0 > 0 as usize {
            if (heightmap[next_position.0 - 1 as usize][next_position.1] <= heightmap[next_position.0][next_position.1] + 1) & !(shortest_visited.contains_key(&(next_position.0 - 1 as usize, next_position.1))) {
                // Add point above
                if !to_visit.contains(&((next_position.0 - 1 as usize, next_position.1), steps)) {
                    to_visit.push(((next_position.0 - 1 as usize, next_position.1), steps));
                }
            }
        }
        if next_position.0 < (heightmap.len() - 1) as usize {
            if (heightmap[next_position.0 + 1 as usize][next_position.1] <= heightmap[next_position.0][next_position.1] + 1) & !(shortest_visited.contains_key(&(next_position.0 + 1 as usize, next_position.1))) {
                // Add point below
                if !to_visit.contains(&((next_position.0 + 1 as usize, next_position.1), steps)) {
                    to_visit.push(((next_position.0 + 1 as usize, next_position.1), steps));
                }
            }
        }
        if next_position.1 > 0 as usize {
            if (heightmap[next_position.0][next_position.1 - 1 as usize] <= heightmap[next_position.0][next_position.1] + 1) & !(shortest_visited.contains_key(&(next_position.0, next_position.1 - 1 as usize))) {
                // Add point to left 
                if !to_visit.contains(&((next_position.0, next_position.1 - 1 as usize), steps)) {
                    to_visit.push(((next_position.0, next_position.1 - 1 as usize), steps));
                }
            }
        }
        if next_position.1 < (heightmap[0].len() - 1) as usize {
            if (heightmap[next_position.0][next_position.1 + 1 as usize] <= heightmap[next_position.0][next_position.1] + 1) & !(shortest_visited.contains_key(&(next_position.0, next_position.1 + 1 as usize))) {
                // Add point to right
                if !to_visit.contains(&((next_position.0, next_position.1 + 1 as usize), steps)) {
                    to_visit.push(((next_position.0, next_position.1 + 1 as usize), steps));
                }
            }
        }
    }
    shortest
}

// fn depth_first_search(heightmap: Vec<Vec<u32>>, visited: Vec<Vec<bool>>, current: (usize, usize), goal: (usize, usize), length: u32) -> u32 {
//     // Initialise to large, but not large enough to cause overflow
//     let mut up_length = u32::MAX / 2;
//     let mut down_length = u32::MAX / 2;
//     let mut left_length = u32::MAX / 2;
//     let mut right_length = u32::MAX / 2;

//     if (current.0 == goal.0) & (current.1 == goal.1) {
//         return length;
//     }
//     if current.0 > 0 as usize {
//         if (heightmap[current.0 - 1 as usize][current.1] <= heightmap[current.0][current.1] + 1) & !(visited[current.0 - 1 as usize][current.1]) {
//             // Go up
//             let new_pos = (current.0 - 1, current.1);
//             let mut visited_new = visited.clone();
//             visited_new[new_pos.0][new_pos.1] = true;
//             up_length = length + 1;
//             up_length = depth_first_search(heightmap.clone(), visited_new, new_pos, goal, up_length);
//         }
//     }
//     if current.0 < (heightmap.len() - 1) as usize {
//         if (heightmap[current.0 + 1 as usize][current.1] <= heightmap[current.0][current.1] + 1) & !(visited[current.0 + 1 as usize][current.1]) {
//             // Go down
//             let new_pos = (current.0 + 1, current.1);
//             let mut visited_new = visited.clone();
//             visited_new[new_pos.0][new_pos.1] = true;
//             down_length = length + 1;
//             down_length = depth_first_search(heightmap.clone(), visited_new, new_pos, goal, down_length);
//         }
//     } 
//     if current.1 > 0 as usize {
//         if (heightmap[current.0][current.1 - 1 as usize] <= heightmap[current.0][current.1] + 1) & !(visited[current.0][current.1 - 1 as usize]) {
//             // Go left
//             let new_pos = (current.0, current.1 - 1);
//             let mut visited_new = visited.clone();
//             visited_new[new_pos.0][new_pos.1] = true;
//             left_length = length + 1;
//             left_length = depth_first_search(heightmap.clone(), visited_new, new_pos, goal, left_length);
//         }
//     }
//     if current.1 < (heightmap[0].len() - 1) as usize {
//         if (heightmap[current.0][current.1 + 1 as usize] <= heightmap[current.0][current.1] + 1) & !(visited[current.0][current.1 + 1 as usize]) {
//             // Go right
//             let new_pos = (current.0, current.1 + 1);
//             let mut visited_new = visited.clone();
//             visited_new[new_pos.0][new_pos.1] = true;
//             right_length = length + 1;
//             right_length = depth_first_search(heightmap.clone(), visited_new, new_pos, goal, right_length);
//         }
//     } 


//     up_length.min(down_length).min(left_length).min(right_length)
// }