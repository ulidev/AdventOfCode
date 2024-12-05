from functools import reduce


def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        criteria, orders = file.read().split('\n\n')
    criteria = criteria.split()
    solutions = orders.split()
    return criteria, solutions

def is_correct_ordered(dependencies, solution):
    seen = set()
    for page in solution:
        if (not page not in dependencies) and set(dependencies[page]) & seen:
            return False
        seen.add(page)

    return True

def part_one():
    criteria, solutions = get_input()
    dependencies = {}
    criteria = [[int(c.split('|')[0]), int(c.split('|')[1])] for c in criteria]
    for x, y in criteria:
        if x in dependencies:
            dependencies[x].append(y)
        else:
            dependencies[x] = [y]

    solutions = [[int(el) for el in s.split(',')] for s in solutions]
    filtered_solutions = list(filter(lambda x: is_correct_ordered(dependencies, x), solutions))
    reduced = reduce(lambda x, y: x + y[int(len(y)/2)], filtered_solutions, 0)
    return reduced

def order_correctly(dependencies, solution):
    seen = set()
    new_solution = []
    for page in solution:
        if page in dependencies:
            setdiff = set(dependencies[page]) & seen
            if setdiff:
                lowest_index_element = min(setdiff, key=lambda x: new_solution.index(x))
                new_solution.insert(new_solution.index(lowest_index_element), page)
            else:
                new_solution.append(page)
        else:
            new_solution.append(page)
        seen.add(page)
    return new_solution

def part_two():
    criteria, solutions = get_input()
    dependencies = {}
    criteria = [[int(c.split('|')[0]), int(c.split('|')[1])] for c in criteria]
    for x, y in criteria:
        if x in dependencies:
            dependencies[x].append(y)
        else:
            dependencies[x] = [y]

    solutions = [[int(el) for el in s.split(',')] for s in solutions]
    incorrect = list(filter(lambda x: not is_correct_ordered(dependencies, x), solutions))
    ordered_properly = list(map(lambda x: order_correctly(dependencies, x), incorrect))
    reduced = reduce(lambda x, y: x + y[int(len(y) / 2)], ordered_properly, 0)
    return reduced


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
