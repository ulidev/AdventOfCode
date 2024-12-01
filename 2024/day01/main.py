from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = list(map(lambda x: [int(x[0]), int(x[1])], map(lambda x: x.split('   '), file.read().splitlines())))
    return lines


def part_one():
    lines = get_input()
    left, right = sorted(list(map(lambda x: x[0], lines))), sorted(list(map(lambda x: x[1], lines)))
    paired = list(zip(left, right))
    summed = reduce(lambda x, y: x + abs(y[1] - y[0]), paired, 0)
    return summed


def part_two():
    lines = get_input()
    left, right = sorted(list(map(lambda x: x[0], lines))), sorted(list(map(lambda x: x[1], lines)))
    diffs = list(map(lambda x: x * len(list(filter(lambda y: y == x, left))), right))
    return sum(diffs)


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
