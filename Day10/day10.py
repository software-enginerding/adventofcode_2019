import math
from collections import defaultdict
from sympy.geometry import *

# using the sympy built-in slope function didn't give the correct results, using this one does
def calc_slope(start: Point2D, end: Point2D):
    result = math.atan2(end.x - start.x, start.y - end.y) * 180 / math.pi
    if result < 0:
        return 360 + result
    return result


def map_asteroids():
    with open("input", "r") as data:
        asteroids = []
        line_index = 0
        for line in data.readlines():
            for index, char in enumerate(line):
                if char == "#":
                    asteroids.append(Point(index, line_index))
            line_index += 1
        return asteroids


def part1():
    asteroids = map_asteroids()
    # for each asteroid, calculate all possible slopes between other asteroids
    best = None
    highest_seen = 0
    for index, a in enumerate(asteroids):
        slopes = set()
        for index2, b in enumerate(asteroids):
            if index == index2:
                continue
            s = calc_slope(a, b)
            slopes.add(s)
        seen = len(slopes)
        if seen > highest_seen:
            best = a
            highest_seen = seen
    print(f"Best {best} with count {highest_seen}")


def part2():
    asteroids = map_asteroids()
    # best asteroid determined in part 1
    best_index = asteroids.index(Point(37, 25))
    start = asteroids[best_index]
    slopes = defaultdict(list)
    # group all asteroids by slope from start
    for i, a in enumerate(asteroids):
        if i == best_index:
            continue
        s = calc_slope(start, a)
        slopes[s].append(a)

    # sort each slope list by distance from the start
    for key in slopes.keys():
        slopes[key] = sorted(slopes[key], key=lambda asteroid: start.distance(asteroid))

    sorted_keys = sorted(slopes.keys())
    destroyed_count = 0
    slope_index = 0
    last_destroyed = None
    while destroyed_count < 200:
        # clamp slope index to size of slopes
        if slope_index > len(sorted_keys) - 1:
            slope_index = 0
        last_destroyed = slopes[sorted_keys[slope_index]].pop(0)
        destroyed_count += 1
        slope_index += 1
        print(f"Asteroid at {last_destroyed} destroyed. Count: {destroyed_count}")

    print(last_destroyed.x * 100 + last_destroyed.y)


part1()
part2()