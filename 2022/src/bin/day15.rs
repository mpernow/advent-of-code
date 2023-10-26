use std::fs::File;
use std::io::{BufRead, BufReader};
use std::collections::HashSet;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> u32 {
    let f = File::open("./input/data_15").expect("Unable to open file");
    let f = BufReader::new(f);

    // let target_y: i32 = 10;
    let target_y: i32 = 2000000;

    let mut x_vals: HashSet<i32> = HashSet::new();
    let mut beacons_on_target: HashSet<i32> = HashSet::new();

    for line in f.lines() {
        if let Ok(s) = line {
            let s_vec: Vec<&str> = s.split(' ').collect::<Vec<&str>>();
            let sensor_x: &i32 = &s_vec[2][2..(s_vec[2].len() - 1)].parse::<i32>().unwrap();
            let sensor_y: &i32 = &s_vec[3][2..(s_vec[3].len() - 1)].parse::<i32>().unwrap();
            let beacon_x: &i32 = &s_vec[8][2..(s_vec[8].len() - 1)].parse::<i32>().unwrap();
            let beacon_y: &i32 = &s_vec[9][2..(s_vec[9].len())].parse::<i32>().unwrap();
            let manhattan_distance = (sensor_x - beacon_x).abs() + (sensor_y - beacon_y).abs();
            let to_target: i32 = (target_y - sensor_y).abs();
            if manhattan_distance == to_target {
                x_vals.insert(*sensor_x);
            } else if manhattan_distance > to_target {
                for x in (-(manhattan_distance - to_target))..(manhattan_distance - to_target + 1) {
                    x_vals.insert(sensor_x + x);
                }
            }
            if *beacon_y == target_y {
                beacons_on_target.insert(*beacon_y);
            }
        }
    }
    for beacon in beacons_on_target.iter() {
        x_vals.take(beacon);
    }
    x_vals.len() as u32
}

fn part2() -> i64 {
    let f = File::open("./input/data_15").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut sensors: Vec<(i32, i32, i32)> = Vec::new();
    // Tuples (x, y, radius)

    // let limit: i32 = 20;
    let limit: i32 = 4_000_000;

    for line in f.lines() {
        if let Ok(s) = line {
            let s_vec: Vec<&str> = s.split(' ').collect::<Vec<&str>>();
            let sensor_x: &i32 = &s_vec[2][2..(s_vec[2].len() - 1)].parse::<i32>().unwrap();
            let sensor_y: &i32 = &s_vec[3][2..(s_vec[3].len() - 1)].parse::<i32>().unwrap();
            let beacon_x: &i32 = &s_vec[8][2..(s_vec[8].len() - 1)].parse::<i32>().unwrap();
            let beacon_y: &i32 = &s_vec[9][2..(s_vec[9].len())].parse::<i32>().unwrap();
            let manhattan_distance = (sensor_x - beacon_x).abs() + (sensor_y - beacon_y).abs();
            sensors.push((*sensor_x, *sensor_y, manhattan_distance));
        }
    }

    for s in sensors.iter() {
        for x in s.0 - s.2 - 1..=s.0 + s.2 + 1 {
            if (x > limit) || (x < 0) {
                break;
            }

            let dy = s.2 - (x - s.0).abs() + 1;
            'loop_y: for y in [s.1 + dy, s.1 - dy] {
                if y <= limit && y >= 0 {
                    for s2 in sensors.iter() {
                        if (s2.0 - x).abs() + (s2.1 - y).abs() <= s2.2 {
                            // If point covered by other sensor, check next y value
                            break 'loop_y;
                        }
                    }
                    return x as i64 * 4_000_000 as i64 + y as i64;
                }
            }
        }
    }
    


    0
}