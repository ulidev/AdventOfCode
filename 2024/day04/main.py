import re
from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def count_els(arr):
    return reduce(lambda x, y: x + len(y), arr, 0)

def get_number_of_matches(arr) -> int:
    pattern = r"(?=(XMAS|SAMX))"
    return sum(list(map(lambda x: len(re.findall(pattern, x)), arr)))

def part_one():
    lines = get_input()
    transposed = ["".join(line) for line in zip(*lines)]

    diagonals_main = {}
    diagonals_secondary = {}

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            diag_main_index = i - j
            if diag_main_index not in diagonals_main:
                diagonals_main[diag_main_index] = []
            diagonals_main[diag_main_index].append(lines[i][j])

            diag_secondary_index = i + j
            if diag_secondary_index not in diagonals_secondary:
                diagonals_secondary[diag_secondary_index] = []
            diagonals_secondary[diag_secondary_index].append(lines[i][j])

    diagonal_main_list = list("".join(v) for v in diagonals_main.values())
    diagonal_inverse_list = list("".join(v) for v in diagonals_secondary.values())

    evaluate_arrays = [lines, transposed, diagonal_inverse_list, diagonal_main_list]

    return reduce(lambda x, y: x + get_number_of_matches(y), evaluate_arrays, 0)


def part_two():
    lines = get_input()
    counter = 0
    for i, r in enumerate(lines):
        for j, c in enumerate(r):
            if c == 'A' and i != 0 and j != 0 and i != len(lines) - 1 and j != len(r) - 1:
                sig_els = [lines[i - 1][j - 1], lines[i - 1][j + 1], lines[i + 1][j - 1], lines[i + 1][j + 1]]
                if (sig_els[0] == 'M' and sig_els[3] == 'S') or (sig_els[0] == 'S' and sig_els[3] == 'M') and (
                        sig_els[1] == 'M' and sig_els[2] == 'S') or (sig_els[1] == 'S' and sig_els[2] == 'M'):
                    counter += 1

    return counter


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
