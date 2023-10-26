struct Snafu(String);

impl From<usize> for Snafu {
    fn from(mut n: usize) -> Self {
        let mut res = Vec::new();

        while n > 0 {
            match n % 5 {
                0 => res.push('0'),
                1 => res.push('1'),
                2 => res.push('2'),
                3 => {
                    res.push('=');
                    // from this point on we need to force the encoding of a larger number
                    // this should force us to "carry the one" in the next division by 5
                    n += 2;
                }
                4 => {
                    res.push('-');
                    n += 1
                }
                _ => unreachable!(),
            };

            // we really just need to make the next division a ceil division
            // in the n%5 = 3 | 4 cases, which could be done by adding 2

            n /= 5;
        }

        Snafu(res.into_iter().rev().collect())
    }
}

impl From<Snafu> for usize {
    fn from(other: Snafu) -> usize {
        let length = other.0.len() as u32;

        let mut res = 0;

        for (i, c) in other.0.chars().enumerate() {
            let place = 5_i64.pow(length - 1 - i as u32);
            let value = match c {
                '0' => 0,
                '1' => 1,
                '2' => 2,
                '-' => -1,
                '=' => -2,
                _ => unreachable!(),
            };
            res += value * place;
        }
        res as usize
    }
}

impl ToString for Snafu {
    fn to_string(&self) -> String {
        self.0.clone()
    }
}

fn solve_day_25(input: &str) -> String {
    let ans: Snafu = input
        .lines()
        .map(|s| Snafu(s.to_string()))
        .map::<usize, _>(Snafu::into)
        .sum::<usize>()
        .into();
    ans.to_string()
}

fn main() {
    let input = include_str!("../../input/data_25");

    let part_1 = solve_day_25(input);

    println!("Bob's console number: {}", part_1);
}

// #[cfg(test)]
// const EXAMPLE_DATA: &str = include_str!("../example.txt");

// #[test]
// fn int_from_snafu() {
//     let i: usize = Snafu("20".to_string()).into();
//     assert_eq!(i, 10);

//     let j: usize = Snafu("1=11-2".to_string()).into();
//     assert_eq!(j, 2022);

//     let k: usize = Snafu("1121-1110-1=0".to_string()).into();
//     assert_eq!(k, 314159265);
// }

// #[test]
// fn snafu_from_int() {
//     assert_eq!(Snafu::from(2022).to_string(), "1=11-2");

//     assert_eq!(Snafu::from(314159265).to_string(), "1121-1110-1=0");
// }

// #[test]
// fn example() {
//     let part_1 = solve_day_25(EXAMPLE_DATA);
//     assert_eq!(part_1, "2=-1=0");
// }