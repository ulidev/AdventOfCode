use std::collections::HashSet;

fn manage_input<'a>() -> Vec<&'a str> {
    let input = include_str!("input.txt");
    let v: Vec<&'a str> = input.split(", ").collect();
    v
}

fn part_two(input: Vec<&str>) -> i32 {
    let mut seek_positions = HashSet::new();
    
    let mut dirx = 0;
    let mut diry = 1;

    let mut x: i32 = 0;
    let mut y: i32 = 0;

    for element in input{
        let dir = element.chars().nth(0).unwrap();
        let steps = element[1..].parse::<i32>().unwrap();

        if dir == 'R'{
            if dirx == 0{
                dirx = diry;
                diry = 0;
            }else{
                diry = -dirx;
                dirx = 0;
            }
        } else {
            if dirx == 0{
                dirx = -diry;
                diry = 0;
            }else{
                diry = dirx;
                dirx = 0;
            }
        }

        for _ in 0..steps{
            x += dirx;
            y += diry;

            if !seek_positions.insert((x, y)){
                return x.abs() + y.abs();
            }
        }

    }

    (x.abs() + y.abs()) as i32
}



fn part_one(input: Vec<&str>) -> i32 {
    let mut dirx = 0;
    let mut diry = 1;

    let mut x = 0;
    let mut y = 0;

    for element in input{
        let dir = element.chars().nth(0).unwrap();
        let steps = element[1..].parse::<i32>().unwrap();

        if dir == 'R'{
            if dirx == 0{
                dirx = diry;
                diry = 0;
            }else{
                diry = -dirx;
                dirx = 0;
            }
        } else {
            if dirx == 0{
                dirx = -diry;
                diry = 0;
            }else{
                diry = dirx;
                dirx = 0;
            }
        }

        x += steps * dirx;
        y += steps * diry;
    }

    (x.abs() + y.abs()) as i32
}

fn main(){
    let input = manage_input();
    
    println!("Part one: {}", part_one(input.clone()));
    println!("Part two: {}", part_two(input.clone()));
}