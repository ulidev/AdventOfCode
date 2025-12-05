class Range:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def contains(self, n: int) -> bool:
        return self.a <= n <= self.b
    
    def merge(self, other: 'Range') -> 'Range | None':
        if self.b < other.a - 1 or other.b < self.a - 1:
            return None
        return Range(min(self.a, other.a), max(self.b, other.b))
    
    def length(self) -> int:
        return self.b - self.a + 1

def parse_ranges(ranges: list[str]) -> list[Range]:
    ranges_out = []
    for line in ranges:
        a, b = map(int, line.split('-'))
        r = Range(a, b)
        ranges_out.append(r)
    return ranges_out

def get_input():
    with open("input.txt", 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
        idx_separator = lines.index('')
        ranges = lines[:idx_separator]
        ingredients = list(map(int, lines[idx_separator + 1:]))
        valid_numbers = parse_ranges(ranges)
    return valid_numbers, ingredients


def part_one(input = get_input()):
    valid_numbers, ingredients = input
    valids = 0
    for i in ingredients:
        for v in valid_numbers:
            if v.contains(i):
                valids += 1
                break
    return valids


def part_two(input = get_input()):
    valid_numbers, _ = input
    final_ranges = [valid_numbers[0]]
    for v in valid_numbers[1:]:
        for f in final_ranges:
            merged = f.merge(v)
            if merged:
                final_ranges.remove(f)
                final_ranges.append(merged)
                for other in final_ranges[:-1]:
                    remerged = merged.merge(other)
                    if remerged:
                        final_ranges.remove(merged)
                        final_ranges.remove(other)
                        final_ranges.append(remerged)
                        merged = remerged
                break
        else:
            final_ranges.append(v)
    return sum(r.length() for r in final_ranges)


if __name__ == "__main__":
    print(f"Part one solution: {part_one()}")
    print(f"Part two solution: {part_two()}")
