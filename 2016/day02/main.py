def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def part_two():
    pass

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
                code_number = new_code if (new_code-1) // 3 == (code_number-1) // 3 else code_number

        code.append(str(code_number))

    return "".join(code)


if __name__ == "__main__":
    print(f"Result of part one: {part_one()}")
