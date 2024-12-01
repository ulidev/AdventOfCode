def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = [[int(el) for el in line.split()] for line in file.read().splitlines()]
    return lines


def is_valid(t):
    s = sorted(t)
    return s[0] + s[1] > s[2]


def part_one():
    lines = get_input()
    valid_lines = list(filter(is_valid, lines))
    return len(valid_lines)


def part_two():
    lines = get_input()
    transformed = [column[i:i + 3] for column in list(zip(*lines)) for i in range(0, len(column), 3)]
    valid_lines = list(filter(is_valid, transformed))
    return len(valid_lines)


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
