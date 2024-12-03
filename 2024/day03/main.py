import re


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def part_one():
    pattern = r"mul\(\d+,\d+\)"
    lines = get_input()
    matches = list(map(lambda x: re.findall(pattern, x), lines ))
    result = 0
    for m in matches:
        vals = list(map(lambda x : x.split('(')[1].split(')')[0].split(','), m))
        vals = [[int(v[0]), int (v[1])] for v in vals]
        for v in vals:
            result = result + v[0] * v[1]
    return result


def part_two():
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    lines = get_input()
    matches = list(map(lambda x: re.findall(pattern, x), lines))
    can_add = True
    result = 0
    for m in matches:
        for el in m:
            if el[:3] == 'mul':
                numbers = el.split('(')[1].split(')')[0].split(',')
                result = result + int(numbers[0]) * int(numbers[1]) if can_add else result
            else:
                if el == "do()":
                    can_add = True
                else:
                    can_add = False
    return result


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
