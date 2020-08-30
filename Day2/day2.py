def run_program(i1, i2):
    with open("input", "r") as data:
        # split string on commas, convert it to integers, store them in a list
        intcode = list(map(lambda x: int(x), data.read().split(",")))
        # replaces 1 with 12 and 2 with 2
        intcode[1] = i1
        intcode[2] = i2
        startIndex = 0
        while intcode[startIndex] != 99:
            opcode = intcode[startIndex]
            v1 = intcode[intcode[startIndex+1]]
            v2 = intcode[intcode[startIndex+2]]
            destination = intcode[startIndex+3]
            if opcode == 1:
                # do addition
                intcode[destination] = v1 + v2
            elif opcode == 2:
                intcode[destination] = v1 * v2
            else:
                print("Unknown Opcode")
                break

            # increment starting index
            startIndex += 4

        return intcode[0]


print(run_program(12, 2))

# find starting values that give 19690720
for x in range(0, 100):
    for y in range(0, 100):
        if run_program(x, y) == 19690720:
            print(f"{x},{y}")
