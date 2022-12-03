use regex::Regex;
use std::fs;

fn main() {
    let rawdata = fs::read_to_string(r"..\..\files\AoC22-d1.txt").expect("Error Reading File");

    let re = Regex::new(r"\r\n\r\n").unwrap();
    let data: Vec<&str> = re.split(&rawdata).collect();

    let mut nums: Vec<i32> = Vec::new();
    for item in &data {
        let sum: i32 = item
            .lines()
            .map(|x| x.trim().parse::<i32>().unwrap())
            .collect::<Vec<i32>>()
            .iter()
            .sum();
        nums.push(sum);
    }

    nums.sort();
    nums.reverse();

    println!("{}", data.len());
    println!("Answer1: {}", nums[0]);
    let ans2 = nums[0] + nums[1] + nums[2];
    println!("Answer2: {}", ans2);
}
