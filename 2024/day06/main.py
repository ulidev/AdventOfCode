from collections import defaultdict
from copy import deepcopy

import numpy as np


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = np.array(file.read().splitlines())
    return lines


def input_to_array(lines):
    return np.array([[c for c in line] for line in lines])

def out_of_bounds(matrix, position):
    return position[0] < 0 or position[1] < 0 or position[0] >= len(matrix) or position[1] >= len(matrix[0])

def part_one():
    lines = get_input()
    matrix = input_to_array(lines)
    direction = (-1, 0)

    position = np.where(matrix == '^')
    position = tuple(zip(position[0], position[1]))[0]

    visited_dict = defaultdict(set)

    visited_dict[position].add(tuple(direction))
    while True:
        next_position = list(map(lambda x: x[0] + x[1], zip(direction, position)))
        if out_of_bounds(matrix, next_position):
            break

        next_value = matrix[next_position[0]][next_position[1]]

        if next_value == '#':
            direction = rotate_right(direction)
            continue

        position = next_position
        visited_dict[tuple(position)].add(tuple(direction))

    return len(visited_dict.keys())


def rotate_right(direction):
    return direction[1], -direction[0]


def test_loop(matrix, position: tuple[int, int], direction: tuple[int, int], visited_dict):
    visited_dict_copy = deepcopy(visited_dict)

    while True:
        new_position = tuple(map(lambda x: x[0] + x[1], zip(direction, position)))
        if out_of_bounds(matrix, new_position):
            break

        if new_position in visited_dict_copy and direction in visited_dict_copy[new_position]:
            return True

        new_value = matrix[new_position[0]][new_position[1]]
        if new_value == '#':
            direction = rotate_right(direction)
            visited_dict_copy[tuple(position)].add(tuple(direction))
            continue

        position = new_position
        visited_dict_copy[tuple(position)].add(tuple(direction))

    return False


def part_two():
    lines = get_input()
    matrix = input_to_array(lines)

    position = np.where(matrix == '^')
    position = tuple(zip(position[0], position[1]))[0]
    direction = (-1, 0)

    visited_dict = defaultdict(set)
    visited_dict[position].add(tuple(direction))

    result_set = set()

    while True:
        next_position = tuple(a + b for a, b in zip(position, direction))
        if out_of_bounds(matrix, next_position):
            break

        next_value = matrix[next_position[0]][next_position[1]]

        # If we hit a wall, we need to rotate
        if next_value == '#':
            direction = rotate_right(direction)
            continue

        if next_position not in visited_dict:
            matrix[next_position[0]][next_position[1]] = '#'  # Mark the position as visited

            if test_loop(matrix, position, direction, visited_dict):
                result_set.add(tuple(next_position))

            matrix[next_position[0]][next_position[1]] = '.'  # Reset the value

        position = next_position
        visited_dict[position].add(tuple(direction))

    return len(result_set)


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
