from itertools import permutations
from intcode_computer import IntcodeComputer


def part1():
    with open("input", "r") as data:
        text = data.read()
        best = -9999999999999
        for p in list(permutations(range(0, 5))):
            print(p)
            last_output = 0
            for i in p:
                last_output = IntcodeComputer(text, i).run_program([last_output])

            best = max(best, last_output)

        print(best)

def run_feedback_loop(p, text):
    print(p)
    amps = [IntcodeComputer(text, p[0]),
            IntcodeComputer(text, p[1]),
            IntcodeComputer(text, p[2]),
            IntcodeComputer(text, p[3]),
            IntcodeComputer(text, p[4])]
    last_output = 0
    while last_output is not None:
        for i in range(0, len(p)):
            output = amps[i].run_program([last_output])
            print(f"output {output}")
            if output is None:
                print(last_output)
                return last_output

            last_output = output



def part2():
    with open("input", "r") as data:
        text = data.read()
        best = -9999999999999
        for p in list(permutations(range(5, 10))):
            print(p)
            best = max(best, run_feedback_loop(p, text))

        print(best)


part1()
part2()
