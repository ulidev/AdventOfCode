from functools import reduce
import textwrap

def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = [tuple(map(int, r.split('-'))) for r in file.read().strip().split(',')]
    return lines

def is_valid(number, times = 2):
    if len(str(number)) % times != 0:
        return False
    chunk_size = len(str(number)) // times
    equally_splitted = textwrap.wrap(str(number), chunk_size)
    return len(set(equally_splitted)) == 1

def expand_numbers(ranges) -> list[int]:
    start, end = ranges
    expanded = []
    for number in range(start, end+1):
        expanded.append(number)
    return expanded

def part_one():
    data = get_input()
    expanded_numbers = [n for r in data for n in expand_numbers(r)]
    result = reduce(lambda acc, x: acc + (x if is_valid(x, 2) else 0) , expanded_numbers, 0)
    return result


def part_two():
    data = get_input()
    expanded_numbers = [n for r in data for n in expand_numbers(r)]
    cumsum = 0
    for num in expanded_numbers:
        num_len = len(str(num))
        i = num_len
        while i > 1:
            if is_valid(number=num, times=i):
                # print(f"i: {i}, Num: {num}")
                cumsum += num
                break
            i -= 1
    return cumsum


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
