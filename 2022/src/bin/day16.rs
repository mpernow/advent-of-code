use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;
use regex::Regex;
use std::collections::HashMap;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

// #[derive(Debug)]
// struct State {
//     time: u32,
//     position: String,
//     opened: Vec<String>,
//     flowrate: u32,
//     total_flow: u32,
// }

fn part1() -> u32 {
    let f = File::open("./input/data_16").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut flowrates: HashMap<String, u32> = HashMap::new();
    let mut neighbours: HashMap<String, Vec<String>> = HashMap::new();
    let mut valves: Vec<String> = Vec::new();

    for line in f.lines() {
        if let Ok(s) = line {
            let valve = &s[6..8].to_string();
            let re_num: Regex = Regex::new(r"\d+").unwrap();
            let flowrate = re_num.find(&s).unwrap().as_str().parse::<u32>().unwrap();
            let leads_to: Vec<String> = s.split(" ").collect::<Vec<&str>>()[9..].iter().map(|s| s[..2].to_string()).collect::<Vec<String>>();
            flowrates.insert((*valve.clone()).to_string(), flowrate);
            neighbours.insert((*valve.clone()).to_string(), leads_to);
            valves.push(valve.to_string());
        }
    }
    // println!("{:?}", flowrates);
    // println!("{:?}", neighbours);

    // Compute all the distances
    let mut distances: HashMap<String, HashMap<String, u32>> = HashMap::new();
    for valve in valves.clone() {
        let mut from_this: HashMap<String, u32> = HashMap::new();
        let starting_neighbours = neighbours.get(&valve).unwrap();
        let mut queue: Vec<(String, u32)> = Vec::new();
        for n in starting_neighbours {
            queue.push((n.to_string(), 1));
        }
        while queue.len() > 0
        {
            let this = queue.remove(0);
            from_this.insert(this.0.clone(), this.1);
            let new_neighbs = neighbours.get(&this.0).unwrap();
            for n in new_neighbs {
                if (!from_this.contains_key(n)) && !(n == &valve) {
                    queue.push((n.to_string(), this.1 + 1));
                }
            }
        }
        distances.insert(valve.to_string(), from_this);
    }
    // println!("{:?}", distances);

    let to_open: Vec<String> = valves.iter().filter(|x| flowrates.get(x.clone()).unwrap() > &0).map(|x| x.to_string()).collect();
    // println!("{:?}", to_open);

    // BFS
    // state = (Current position, closed valves, total flow, time left)
    let mut best_flow: u32 = 0;
    let start: (String, Vec<String>, u32, u32) = ("AA".to_string(), to_open, 0, 30);
    let mut queue: Vec<(String, Vec<String>, u32, u32)> = vec![start];
    while queue.len() > 0 {
        let state = queue.remove(0);
        if state.3 == 0 {
            continue;
        }
        // println!("{:?}", state);
        for i in 0..state.1.len() {
            let mut new_to_open = state.1.clone();
            let valve = new_to_open.remove(i);
            // Total flow contribution of this valve during the whole time, set to zero if not enough time
            let mut time_left: u32 = 0;
            if state.3 > *distances.get(&state.0).unwrap().get(&valve).unwrap() {
                time_left = state.3 - distances.get(&state.0).unwrap().get(&valve).unwrap() - 1;
            }
            let flow_contribution = time_left * flowrates.get(&valve).unwrap();
            if time_left > 0 {
                queue.push((valve, new_to_open, state.2 + flow_contribution, time_left));
            }
            if flow_contribution + state.2 > best_flow {
                best_flow = flow_contribution + state.2;
            }
        }
    }
    // println!("{best_flow}");

    //// The below should work, but is too slow!
    // let start_state: State = State { time: 0, position: "AA".to_string(), opened: Vec::new(), flowrate: 0, total_flow: 0};
    // let mut queue: Vec<State> = vec![start_state];
    // let num_steps: u32 = 30;
    // loop {
    //     let state = queue.remove(0);
    //     println!("{:?}", state);
    //     if state.time == num_steps {
    //         // Put it back to keep record
    //         queue.push(state);
    //         break;
    //     }
    //     if state.opened.len() == flowrates.len() {
    //         // All opened. Stay here, increment time and flowrate
    //         queue.push(State {time: state.time + 1,
    //                           position: state.position.clone(),
    //                           opened: state.opened,
    //                           flowrate: state.flowrate,
    //                           total_flow: state.total_flow + state.flowrate});
    //         continue;
    //     }
    //     if (!state.opened.contains(&state.position)) && (flowrates.get(&state.position).unwrap() > &(0 as u32)) {
    //         // Add opening the valve to queue
    //         let mut new_opened = state.opened.clone();
    //         new_opened.push(state.position.clone());
    //         queue.push(State {time: state.time + 1,
    //                           position: state.position.clone(),
    //                           opened: new_opened,
    //                           flowrate: state.flowrate + flowrates.get(&state.position).unwrap(),
    //                           total_flow: state.total_flow + state.flowrate});
    //     }
    //     // Add all neighbours to queue
    //     let leads_to = neighbours.get(&state.position).unwrap();
    //     for neighbour in leads_to {
    //         queue.push(State {time: state.time + 1,
    //                         position: neighbour.clone(),
    //                         opened: state.opened.clone(),
    //                         flowrate: state.flowrate,
    //                         total_flow: state.total_flow + state.flowrate});
    //     }
    // }
    // println!("{:?}", queue.len());

    best_flow
}

fn part2() -> u32 {
    let f = File::open("./input/data_16").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut flowrates: HashMap<String, u32> = HashMap::new();
    let mut neighbours: HashMap<String, Vec<String>> = HashMap::new();
    let mut valves: Vec<String> = Vec::new();

    for line in f.lines() {
        if let Ok(s) = line {
            let valve = &s[6..8].to_string();
            let re_num: Regex = Regex::new(r"\d+").unwrap();
            let flowrate = re_num.find(&s).unwrap().as_str().parse::<u32>().unwrap();
            let leads_to: Vec<String> = s.split(" ").collect::<Vec<&str>>()[9..].iter().map(|s| s[..2].to_string()).collect::<Vec<String>>();
            flowrates.insert((*valve.clone()).to_string(), flowrate);
            neighbours.insert((*valve.clone()).to_string(), leads_to);
            valves.push(valve.to_string());
        }
    }
    // println!("{:?}", flowrates);
    // println!("{:?}", neighbours);

    // Compute all the distances
    let mut distances: HashMap<String, HashMap<String, u32>> = HashMap::new();
    for valve in valves.clone() {
        let mut from_this: HashMap<String, u32> = HashMap::new();
        let starting_neighbours = neighbours.get(&valve).unwrap();
        let mut queue: Vec<(String, u32)> = Vec::new();
        for n in starting_neighbours {
            queue.push((n.to_string(), 1));
        }
        while queue.len() > 0
        {
            let this = queue.remove(0);
            from_this.insert(this.0.clone(), this.1);
            let new_neighbs = neighbours.get(&this.0).unwrap();
            for n in new_neighbs {
                if (!from_this.contains_key(n)) && !(n == &valve) {
                    queue.push((n.to_string(), this.1 + 1));
                }
            }
        }
        distances.insert(valve.to_string(), from_this);
    }
    // println!("{:?}", distances);

    let to_open: Vec<String> = valves.iter().filter(|x| flowrates.get(x.clone()).unwrap() > &0).map(|x| x.to_string()).collect();
    // println!("{:?}", to_open);

    // Partition the vector into all subsets
    let mut partitions: Vec<(Vec<String>, Vec<String>)> = Vec::new();
    // Limit the number of subsets to those that have somewhat equal numbers of elements
    for n in to_open.len()/4..=to_open.len()/2 {
        let combs = to_open.iter().combinations(n);
        for me in combs {
            let elephant = to_open.iter().filter(|x| !me.contains(x)).map(|x| x.to_string()).collect::<Vec<String>>();
            // println!("{:?}, {:?}", me, elephant);
            partitions.push((me.iter().map(|x| x.to_string()).collect::<Vec<String>>(), elephant));
        }
    }
    let num_partitions = partitions.len();

    // TODO Run this twice, with the two partitions. Loop over all possible partitions
    // BFS
    // state = (Current position, closed valves, total flow, time left)
    let mut best_flow: u32 = 0;
    let mut counter = 0;
    for partition in partitions {
        println!("Iteration {}/{}", counter, num_partitions);
        counter += 1;
        let start_me: (String, Vec<String>, u32, u32) = ("AA".to_string(), partition.0.clone(), 0, 26);
        let start_elephant: (String, Vec<String>, u32, u32) = ("AA".to_string(), partition.1.clone(), 0, 26);

        let mut best_me: u32 = 0;
        let mut best_elephant: u32 = 0;

        let mut queue: Vec<(String, Vec<String>, u32, u32)> = vec![start_me];
        while queue.len() > 0 {
            let state = queue.remove(0);
            if state.3 == 0 {
                continue;
            }
            // println!("{:?}", state);
            for i in 0..state.1.len() {
                let mut new_to_open = state.1.clone();
                let valve = new_to_open.remove(i);
                // Total flow contribution of this valve during the whole time, set to zero if not enough time
                let mut time_left: u32 = 0;
                if state.3 > *distances.get(&state.0).unwrap().get(&valve).unwrap() {
                    time_left = state.3 - distances.get(&state.0).unwrap().get(&valve).unwrap() - 1;
                }
                let flow_contribution = time_left * flowrates.get(&valve).unwrap();
                if time_left > 0 {
                    queue.push((valve, new_to_open, state.2 + flow_contribution, time_left));
                }
                if flow_contribution + state.2 > best_me{
                    best_me = flow_contribution + state.2;
                }
            }
        }
        let mut queue: Vec<(String, Vec<String>, u32, u32)> = vec![start_elephant];
        while queue.len() > 0 {
            let state = queue.remove(0);
            if state.3 == 0 {
                continue;
            }
            // println!("{:?}", state);
            for i in 0..state.1.len() {
                let mut new_to_open = state.1.clone();
                let valve = new_to_open.remove(i);
                // Total flow contribution of this valve during the whole time, set to zero if not enough time
                let mut time_left: u32 = 0;
                if state.3 > *distances.get(&state.0).unwrap().get(&valve).unwrap() {
                    time_left = state.3 - distances.get(&state.0).unwrap().get(&valve).unwrap() - 1;
                }
                let flow_contribution = time_left * flowrates.get(&valve).unwrap();
                if time_left > 0 {
                    queue.push((valve, new_to_open, state.2 + flow_contribution, time_left));
                }
                if flow_contribution + state.2 > best_elephant{
                    best_elephant = flow_contribution + state.2;
                }
            }
        }
        println!("{}", best_me + best_elephant);
        if best_me + best_elephant > best_flow {
            best_flow = best_me + best_elephant;
        }
    }

    best_flow
}