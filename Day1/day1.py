import math


def calculateMass(input):
    # divide by 3
    mass = int(input) / 3
    # round down
    mass = math.floor(mass)
    # subtract 2
    mass = mass - 2
    # add to total
    return max(mass, 0)


def part1():
    with open("input", "r") as data:
        total = 0
        for line in data.readlines():
            # calculate for each line, then add to total
            total += calculateMass(line)

        print(total)


def part2():
    with open("input", "r") as data:
        total = 0
        for line in data.readlines():
            initialMass = calculateMass(line)
            total += initialMass
            additionalMass = calculateMass(initialMass)
            while(additionalMass > 0):
                total += additionalMass
                additionalMass = calculateMass(additionalMass)


        print(total)

part1()
part2()