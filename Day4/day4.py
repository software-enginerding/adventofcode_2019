def has_two_adjacent(v: str):
    for i in range(len(v)-1):
        if v[i] == v[i+1]:
            return True
    return False

def has_one_pair_of_numbers(v: str):
    counts = {}
    for c in v:
        counts[c] = counts.get(c, 0) + 1

    return 2 in counts.values()


def is_always_increasing(v: str):
    for i in range(len(v)-1):
        if int(v[i]) > int(v[i+1]):
            return False
    return True


def part1():
    start = 356261
    end = 846303
    count = 0
    for v in range(start, end+1):
        if has_two_adjacent(str(v)) and is_always_increasing(str(v)):
            count += 1

    print(count)


def part2():
    start = 356261
    end = 846303
    count = 0
    for v in range(start, end+1):
        if has_two_adjacent(str(v)) and is_always_increasing(str(v)) and has_one_pair_of_numbers(str(v)):
            count += 1

    print(count)


part2()