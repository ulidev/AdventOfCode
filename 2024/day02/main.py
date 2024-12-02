import numpy as np


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def part_one():
    lines = get_input()
    arrays = [line.split(' ') for line in lines]
    arrays = [np.diff(np.array(array).astype(int)) for array in arrays]
    filtered = [
        np.all((abs(a) >= 1) & (abs(a) <= 3)) and (np.all(a > 0) or np.all(a < 0))
        for a in arrays
    ]
    return sum(filtered)


def is_valid(a):
    return np.all((abs(a) >= 1) & (abs(a) <= 3)) and (np.all(a > 0) or np.all(a < 0))


def part_two():
    lines = get_input()

    n_feasible = 0
    for line in lines:
        nparr = np.array(line.split(' ')).astype(int)
        diff = np.diff(nparr)
        if is_valid(diff):
            n_feasible += 1
        else:
            for i in range(0, len(nparr)):
                diffi = np.diff(np.delete(nparr, i))
                if is_valid(diffi):
                    n_feasible += 1
                    break

    return n_feasible


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
