from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        lines = list(map(lambda x: x.split(': '), lines))
        lines = tuple(map(lambda x: (int(x[0]), [int(i) for i in x[1].split()]), lines))
    return lines


def is_feasible(case: list[int, tuple[int]]) -> bool:
    target, values = case

    operators = ['+', '*']
    operators_combination = []
    for i in range(0, len(operators) ** (len(values) - 1)):
        operators_combination.append(
            [operators[(i // len(operators) ** j) % len(operators)] for j in range(len(values) - 1)])

    for op in operators_combination:
        zipped = list(zip(op, values[1:]))
        result = reduce(lambda x, y: eval(f"{x} {y[0]} {y[1]}"), zipped, values[0])
        if result == target:
            return True

    return False


def part_one():
    lines = get_input()
    result = reduce(lambda x, y: x + y[0], list(filter(lambda x: is_feasible(x), lines)), 0)
    return result


def is_feasible_p2_caching(case):
    target, values = case
    dp = [set() for _ in range(len(values) + 1)]
    dp[1].add(values[0])

    for i in range(2, len(values) + 1):
        num = values[i - 1]
        for prev_result in dp[i - 1]:
            new_res = prev_result + num
            if new_res <= 10 * target:
                dp[i].add(new_res)

            new_res = prev_result * num
            if new_res <= 10 * target:
                dp[i].add(new_res)

            digit_count = len(str(num))
            new_res = prev_result * (10 ** digit_count) + num
            if new_res <= 10 * target:
                dp[i].add(new_res)

    return target in dp[len(values)]


def is_feasible_p2(case: tuple[int, tuple[int]]) -> bool:
    target, values = case

    operators = ['+', '*', '||']
    operators_combination = []
    for i in range(0, len(operators) ** (len(values) - 1)):
        operators_combination.append(
            [operators[(i // len(operators) ** j) % len(operators)] for j in range(len(values) - 1)])

    for op in operators_combination:
        zipped = list(zip(op, values[1:]))
        result = values[0]
        for r in zipped:
            if r[0] == '||':
                result = int(eval(f"{str(result) + str(r[1])}"))
            else:
                result = eval(f"{result} {r[0]} {r[1]}")

            if result > target:
                break

        if result == target:
            return True

    return False


def part_two():
    lines = get_input()
    result = reduce(lambda x, y: x + y[0], list(filter(lambda x: is_feasible_p2_caching(x), lines)), 0)
    return result


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
