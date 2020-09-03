from intcode_computer import IntcodeComputer


def part1():
    with open("input", "r") as data:
        text = data.read()
        comp = IntcodeComputer(text)
        print(comp.run_program([1]))


def part2():
    with open("input", "r") as data:
        text = data.read()
        comp = IntcodeComputer(text)
        print(comp.run_program([2]))


part2()


