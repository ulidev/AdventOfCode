from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        lines = [int(l[1:]) * (-1 if l[0] == 'L' else 1) for l in lines]
    return lines


def part_one():
    dial = 50
    data = get_input()
    
    zeros = 0
    for op in data:
        new_dial = dial + op
        new_dial = new_dial%100
        if new_dial == 0:
            zeros += 1
        dial = new_dial

    return zeros


def part_two():
    dial = 50
    data = get_input()
    
    zeros = 0
    for op in data:
        new_dial = dial + op
        mod_dial = new_dial%100
        zeros += abs(new_dial//100)
        if dial == 0 and new_dial < 0:
            zeros -= 1
        if mod_dial == 0 and (dial < 0 or op < 0):
            zeros += 1
        dial = mod_dial


    return zeros


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}") # 6536 too high. 6405 incorrect. 6124 incorrect
