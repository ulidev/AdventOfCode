from collections import defaultdict
from itertools import combinations


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = [[c for c in l]for l in file.read().splitlines()]
    return lines

def get_antinodes_p1(antennas : dict[str, set[tuple[int, int]]], max_x : int, max_y : int) -> set[tuple[int, int]]:
    antinodes = set()
    for a in antennas.values():
        coordinates_combination = set(combinations(a, 2))
        for c1, c2 in coordinates_combination:
            diff = (c1[0] - c2[0], c1[1] - c2[1])
            if (0 <= c1[0] + diff[0] < max_x) and (0 <= c1[1] + diff[1] < max_y):
                antinodes.add((c1[0] + diff[0], c1[1] + diff[1]))
            if (0 <= c2[0] - diff[0] < max_x) and (0 <= c2[1] - diff[1] < max_y):
                antinodes.add((c2[0] - diff[0], c2[1] - diff[1]))

    return antinodes

def get_antennas(matrix: list[list[str]]) -> dict[str, set[tuple[int, int]]]:
    antennas = defaultdict(set)

    for i, line in enumerate(matrix):
        for j, c in enumerate(line):
            if c != '.':
                antennas[c].add((i,j))

    return antennas

def part_one():
    matrix = get_input()
    antennas = get_antennas(matrix)
    antinodes = get_antinodes_p1(antennas, len(matrix[0]), len(matrix))
    return len(antinodes)


def get_antinodes_p2(antennas : dict[str, set[tuple[int, int]]], max_x : int, max_y : int) -> set[tuple[int, int]]:
    antinodes = set()
    for a in antennas.values():
        coordinates_combination = set(combinations(a, 2))
        for c1, c2 in coordinates_combination:
            diff = (c1[0] - c2[0], c1[1] - c2[1])

            n = 0
            while (0 <= c1[0] + n*diff[0] < max_x) and (0 <= c1[1] + n*diff[1] < max_y):
                antinodes.add((c1[0] + n*diff[0], c1[1] + n*diff[1]))
                n += 1

            n = 0
            while (0 <= c2[0] - n*diff[0] < max_x) and (0 <= c2[1] - n*diff[1] < max_y):
                antinodes.add((c2[0] - n*diff[0], c2[1] - n*diff[1]))
                n += 1

    return antinodes

def part_two():
    matrix = get_input()
    antennas = get_antennas(matrix)
    antinodes = get_antinodes_p2(antennas, len(matrix[0]), len(matrix))
    return len(antinodes)


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
