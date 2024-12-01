from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def char_to_dir(c) -> tuple[int, int]:
    match c:
        case 'U':
            return -1, 0
        case 'D':
            return 1, 0
        case 'L':
            return 0, -1
        case 'R':
            return 0, 1


def part_two():
    lines = get_input()
    table = [
        [-1, -1, 1, -1, -1],
        [-1, 2, 3, 4, -1],
        [5, 6, 7, 8, 9],
        [-1, 'A', 'B', 'C', -1],
        [-1, -1, 'D', -1, -1],
    ]

    def is_valid(t) -> bool:
        if t[0] < 0 or t[0] > 4 or t[1] < 0 or t[1] > 4:
            return False
        if table[t[0]][t[1]] != -1:
            return True

    position = (2, 0)
    set_instructions = [list(map(char_to_dir, line)) for line in lines]

    code = []
    for instructions in set_instructions:
        position = reduce(lambda acc, element: (acc[0] + element[0], acc[1] + element[1]) if is_valid(
            (acc[0] + element[0], acc[1] + element[1])) else acc, instructions, position)
        code.append(str(table[position[0]][position[1]]))

    return "".join(code)


def part_one():
    lines = get_input()
    code = []
    code_number = 5
    for line in lines:
        for c in line:
            if c == 'U' or c == "D":
                new_code = code_number - 3 if c == 'U' else code_number + 3
                code_number = new_code if new_code in range(1, 10) else code_number
            else:
                new_code = code_number - 1 if c == 'L' else code_number + 1
                code_number = new_code if (new_code - 1) // 3 == (code_number - 1) // 3 else code_number

        code.append(str(code_number))

    return "".join(code)


if __name__ == "__main__":
    print(f"Result of part one: {part_one()}")
    print(f"Result of part two: {part_two()}")
