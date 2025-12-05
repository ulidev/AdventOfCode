import numpy as np

def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = [[c == '@' for c in l] for l in file.read().splitlines()]
        matrix = np.matrix(lines)
    return matrix

def count_surroundings(matrix, i, j):
    count = 0
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue
            if i + di < 0 or i + di >= matrix.shape[0]:
                continue
            if j + dj < 0 or j + dj >= matrix.shape[1]:
                continue
            if matrix[i + di, j + dj]:
                count += 1
    return count


def part_one():
    data = get_input()
    less_than_four = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            surroundings = count_surroundings(data, i, j)
            if data[i, j] and surroundings < 4:
                # print(f"Position ({i}, {j}) has {surroundings} surrounding '@'")
                less_than_four += 1
    return less_than_four

def process_surroundings(matrix, i, j, threshold=4):
    less_than_threshold = 0
    copied_matrix = matrix.copy()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            surroundings = count_surroundings(matrix, i, j)
            if matrix[i, j] and surroundings < 4:
                # print(f"Position ({i}, {j}) has {surroundings} surrounding '@'")
                less_than_threshold += 1
                copied_matrix[i, j] = False

    return copied_matrix, less_than_threshold

def part_two():
    data = get_input()
    less_than_threshold = 1
    removed_count = 0
    while less_than_threshold > 0:
        data, less_than_threshold = process_surroundings(data, 0, 0, threshold=4)
        removed_count += less_than_threshold
    return removed_count


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}") #1999 to high
    print(f"Part two solution: {part_two()}")
