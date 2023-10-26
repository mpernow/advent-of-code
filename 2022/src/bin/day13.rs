use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;
use serde_json::{json, Value};
use std::cmp::Ordering;

fn main() {
    println!("{}", part1());
    println!("{}", part2());
}

fn part1() -> usize {
    let f = File::open("./input/data_13").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut pairs: Vec<(Value, Value)> = Vec::new();

    for lines in &f.lines().chunks(3) {
        let mut tup: (Value, Value) = (json!(null), json!(null));
        for (i, line) in lines.enumerate() {
            if i == 0 {
                tup.0 = serde_json::from_str::<Value>(&(line.expect("Could not parse"))).unwrap();
            } else if i == 1 {
                tup.1 = serde_json::from_str::<Value>(&(line.expect("Could not parse"))).unwrap();
            }
        }
        pairs.push(tup);
    }

    pairs
        .iter()
        .map(|p| compare_jsons(&p.0, &p.1))
        .enumerate()
        .filter(|(_, p)| p.is_some() && matches!(p.unwrap(), Ordering::Less))
        .map(|(i, _)| i + 1)
        .sum::<usize>()
}

fn part2() -> usize {
    let f = File::open("./input/data_13").expect("Unable to open file");
    let f = BufReader::new(f);

    let mut packets: Vec<Value> = Vec::new();

    for lines in &f.lines().chunks(3) {
        for (i, line) in lines.enumerate() {
            if (i == 0) || (i == 1) {
                packets.push(serde_json::from_str::<Value>(&(line.expect("Could not parse"))).unwrap());
            }
        }
    }
    packets.push(json!([[2]]));
    packets.push(json!([[6]]));
    packets.sort_by(|first, second| compare_jsons(first, second).unwrap());

    let ind1 = packets.iter().position(|p| *p == json!([[2]])).unwrap() + 1;
    let ind2 = packets.iter().position(|p| *p == json!([[6]])).unwrap() + 1;
    
    ind1 * ind2
}

fn compare_jsons(first: &Value, second: &Value) -> Option<Ordering> {

    match (first, second) {
        (Value::Number(first), Value::Number(second)) => match first.as_u64().cmp(&second.as_u64()) {
            Ordering::Equal => None,
            order => Some(order),
        },
        (Value::Array(first), Value::Array(second)) => {
            if first.is_empty() || second.is_empty() {
                match first.len().cmp(&second.len()) {
                    Ordering::Equal => None,
                    order => Some(order),
                }
            } else if let Some(v) = compare_jsons(&first[0], &second[0]) {
                Some(v)
            } else {
                compare_jsons(&json!(first[1..]), &json!(second[1..]))
            }
        }
        (Value::Number(first), Value::Array(second)) => compare_jsons(&json!(vec![first]), &json!(second)),
        (Value::Array(first), Value::Number(second)) => compare_jsons(&json!(first), &json!(vec![second])),
        _ => Some(Ordering::Greater),
    }
}