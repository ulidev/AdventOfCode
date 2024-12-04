import re
from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def count_els(arr):
    return reduce(lambda x, y: x + len(y), arr, 0)


def part_one():
    pattern = r"(?=(XMAS))"
    lines = get_input()
    h_matches = list(map(lambda x: re.findall(pattern, x), lines))
    h_i_matches = list(map(lambda x: re.findall(pattern, x[::-1]), lines))
    transposed = ["".join(line) for line in zip(*lines)]
    v_matches = list(map(lambda x: re.findall(pattern, x), transposed))
    v_i_matches = list(map(lambda x: re.findall(pattern, x[::-1]), transposed))

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
    d_matches = list(map(lambda x: re.findall(pattern, x), diagonal_main_list))
    d_i_matches = list(map(lambda x: re.findall(pattern, x[::-1]), diagonal_main_list))

    diagonal_inverse_list = list("".join(v) for v in diagonals_secondary.values())
    d_r_matches = list(map(lambda x: re.findall(pattern, x), diagonal_inverse_list))
    d_r_i_matches = list(map(lambda x: re.findall(pattern, x[::-1]), diagonal_inverse_list))

    count = count_els(h_matches) + count_els(h_i_matches) + count_els(v_matches) + count_els(v_i_matches) + count_els(
        d_matches) + count_els(d_i_matches) + count_els(d_r_matches) + count_els(d_r_i_matches)

    return count


def part_two():
    lines = get_input()
    counter = 0
    for i, r in enumerate(lines):
        for j, c in enumerate(r):
            if c == 'A' and i != 0 and j != 0 and i != len(lines) - 1 and j != len(r) - 1:
                sig_els = [lines[i - 1][j - 1], lines[i - 1][j + 1], lines[i + 1][j - 1], lines[i + 1][j + 1]]
                if (sig_els[0] == 'M' and sig_els[3] == 'S') or (sig_els[0] == 'S' and sig_els[3] == 'M'):
                    if (sig_els[1] == 'M' and sig_els[2] == 'S') or (sig_els[1] == 'S' and sig_els[2] == 'M'):
                        counter += 1

    return counter


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
