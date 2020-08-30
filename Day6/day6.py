orbits = {}

def count_depth(key):
    if key not in orbits:
        return 0

    result = 0
    orbits.setdefault(key, [])
    for k in orbits[key]:
        print(f"Checking {k}")
        result += 1 + count_depth(k)
    return result


def part1():
    with open("input", "r") as data:
        for line in data.readlines():
            a = line.split(")")[0]
            b = line.rstrip().split(")")[1]
            orbits.setdefault(a, [])
            orbits[a].append(b)

        print(orbits)
        total = 0
        for k in orbits.keys():
            total += count_depth(k)
        print(total)


def part2():
    with open("input", "r") as data:
        for line in data.readlines():
            a = line.rstrip().split(")")[1]
            b = line.split(")")[0]
            orbits.setdefault(a, [])
            orbits[a].append(b)
            orbits.setdefault(b, [])
            orbits[b].append(a)

        print(orbits)
        total = 0
        found_santa = False
        # start a the planet we orbit, traverse tree until santa is found
        goal = orbits["SAN"][0]
        to_check = orbits["YOU"]
        has_checked = []
        while not found_santa:
            print(f"Checking: {to_check}")
            if goal in to_check or len(to_check) == 0:
                found_santa = True
                break

            total += 1
            next_set = []
            for p in to_check:
                print(f"Checking children for: {p}")
                if p in orbits and p not in has_checked:
                    has_checked.append(p)
                    next_set.extend(orbits[p])

            to_check = next_set

        print(total)


part2()