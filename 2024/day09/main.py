from functools import reduce
from warnings import simplefilter

from utils.time_it import time_it


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        line = file.read().strip()
    return line

@time_it
def part_one():
    line = get_input()

    files = line[::2]
    file_map = {i: int(f) for i, f in enumerate(files)}
    empty_block = [int(el) for el in line[1::2]]

    final_array = []

    # while file map is not empty
    processing_file = True

    while file_map:
        if file_map and processing_file:
            k = min(file_map.keys())
            v = file_map[k]
            final_array.extend([k] * v)
            del file_map[k]
            processing_file = False

        if empty_block and file_map and not processing_file:
            free_space = empty_block[0]
            k = max(file_map.keys())
            v = file_map[k]
            if v > free_space:
                final_array.extend([k] * free_space)
                file_map[k] -= free_space
            else:
                final_array.extend([k] * v)
                del file_map[k]

            if v >= free_space:
                processing_file = True
                empty_block.pop(0)
            else:
                empty_block[0] -= v

    result = reduce(lambda x, y: x + y[0] * y[1], enumerate(final_array), 0)
    return result


def extend_file(array, file_map):
    k = min(file_map.keys())
    v = file_map[k]
    array.extend([k] * v)
    del file_map[k]

@time_it
def part_two():
    line = get_input()
    line = [int(el) for el in line]

    simplified_array = [(i//2, l) if i%2 == 0 else (-1, l) for i, l in enumerate(line)]

    i = len(simplified_array) - 1
    while i > 0:
        file_id, size = simplified_array[i]
        if file_id == -1:
            i -= 1
            continue
        for j in range(0, i):
            if simplified_array[j][0] == -1 and simplified_array[j][1] >= size:
                simplified_array[j] = (-1, simplified_array[j][1] - size)
                simplified_array[i] = (-1, size)
                simplified_array.insert(j, (file_id, size))
                break
        i-=1

    i = 0
    check_sum = 0
    current_pos = 0
    while i < len(simplified_array):
        file_id, size = simplified_array[i]
        if file_id != -1:
            j = 0
            while j < size:
                check_sum += file_id * (j + current_pos)
                j+= 1
        i += 1
        current_pos += size

    return check_sum


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
