import copy
from collections import defaultdict


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        line = [int(el) for el in file.read().split()]
    return line

def process_element(element) -> int or tuple[int, int]:
    if element == 0:
        return 1
    if len(str(element)) % 2 == 0:
        left = int(str(element)[:len(str(element))//2])
        right = int(str(element)[len(str(element))//2:])
        return left, right
    else:
        return element * 2024

def part_one():
    line = get_input()

    stones = line
    for i in range(0,25):
        new_stones = []
        for element in stones:
            processed = process_element(element)
            if isinstance(processed, tuple):
                new_stones.append(processed[0])
                new_stones.append(processed[1])
            else:
                new_stones.append(processed)
        stones = new_stones


    return len(stones)


def part_two():
    line = get_input()
    stones = line

    queue = [(stone, defaultdict(int, {75: 1})) for stone in stones]
    stone_number = 0
    while queue:
        stone, iterations = queue.pop(0)
        # Get elements which iterations is 0

        if not iterations:
            continue

        next_iterations = defaultdict(int)
        for it, count in iterations.items():
            if it == 0:
                stone_number += count
                continue
            next_iterations[it - 1] += count

        processed = process_element(stone)

        if not next_iterations:
            continue

        def add_or_merge(new_stone, new_its):
            for q_stone, q_its in queue:
                if q_stone == new_stone:
                    for s_it, s_count in new_its.items():
                        q_its[s_it] += s_count
                    return
            queue.append((new_stone, copy.deepcopy(new_its)))

        if isinstance(processed, tuple):
            a, b = processed
            add_or_merge(a, next_iterations)
            add_or_merge(b, next_iterations)
        else:
            add_or_merge(processed, next_iterations)
    return stone_number


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
