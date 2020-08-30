import matplotlib.pyplot as plt
from sympy import *
from sympy.geometry import *


def line_input_to_segment_array(line_input:str):
    segments = []
    # split into commands
    start = Point(0, 0)
    for l in line_input.split(","):
        # check for direction
        direction = l[0]
        value = int(l[1:])
        if direction == "U":
            end = Point(start.x, start.y + value)
            segments.append(Segment(start, end))
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)
        elif direction == "R":
            end = Point(start.x + value, start.y)
            segments.append(Segment(start, end))
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)
        elif direction == "D":
            end = Point(start.x, start.y - value)
            segments.append(Segment(start, end))
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)
        elif direction == "L":
            end = Point(start.x - value, start.y)
            segments.append(Segment(start, end))
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)

    return segments

def line_input_to_points_array(line_input:str):
    points = []
    # split into commands
    start = Point(0, 0)
    points.append(start)
    for l in line_input.split(","):
        # check for direction
        direction = l[0]
        value = int(l[1:])
        if direction == "U":
            end = Point(start.x, start.y + value)
            points.append(end)
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)
        elif direction == "R":
            end = Point(start.x + value, start.y)
            points.append(end)
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)
        elif direction == "D":
            end = Point(start.x, start.y - value)
            points.append(end)
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)
        elif direction == "L":
            end = Point(start.x - value, start.y)
            points.append(end)
            # set start to a new point at current end to avoid object reuse
            start = Point(end.x, end.y)

    return points


def drawLines():
    with open("input.txt", "r") as data:
        line1input = data.readline()
        line2input = data.readline()

        # Visual Representation
        wire1 = line_input_to_points_array(line1input)[:16]
        wire2 = line_input_to_points_array(line2input)[:16]

        # x axis values
        x = []
        # corresponding y axis values
        y = []

        for p in wire1:
            x.append(p.x)
            y.append(p.y)

        # plotting the points
        plt.plot(x, y, label="wire1")

        # x axis values
        x2 = []
        # corresponding y axis values
        y2 = []

        for p in wire2:
            x2.append(p.x)
            y2.append(p.y)

        # plotting the points
        plt.plot(x2, y2, label="wire2")


        # function to show the
        plt.show()


def part1():
    with open("input.txt", "r") as data:
        line1input = data.readline()
        line2input = data.readline()

        # convert points to lines
        wire1 = line_input_to_segment_array(line1input)
        wire2 = line_input_to_segment_array(line2input)
        # iterate over each line to check for intersection
        best_distance = 9999999999999999
        for w1 in wire1:
            for w2 in wire2:
                intersections = w1.intersection(w2)
                if len(intersections) > 0:
                    print(intersections[0])
                    # manhattan distance calculation for each intersection
                    d = abs(intersections[0].x) + abs(intersections[0].y)
                    if d > 0:
                        best_distance = min(d, best_distance)

        print(best_distance)


def part2():
    with open("input.txt", "r") as data:
        line1input = data.readline()
        line2input = data.readline()

        # convert points to lines
        wire1 = line_input_to_segment_array(line1input)
        wire2 = line_input_to_segment_array(line2input)
        origin = Point(0, 0)

        for l in range(len(wire1)):
            segment1 = wire1[:l]
            segment2 = wire2[:l]
            for w1index in range(len(segment1)):
                for w2index in range(len(segment2)):
                    intersections = segment1[w1index].intersection(segment2[w2index])
                    if len(intersections) > 0 and not origin.equals(intersections[0]):
                        print(f"intersection found: {l}, {intersections[0]}")
                        # drop all extra segments past intersection
                        w1 = segment1[:w1index+1]
                        w2 = segment2[:w2index+1]
                        # sum all the segments through intersection, subtract segment past intersection
                        w1dis = sum(map(lambda x: x.length, w1)) - Segment(w1[-1].p2, intersections[0]).length
                        w2dis = sum(map(lambda x: x.length, w2)) - Segment(w2[-1].p2, intersections[0]).length
                        print(w1dis)
                        print(w2dis)
                        print(w1dis + w2dis)
                        return


part2()