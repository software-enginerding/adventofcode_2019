def run_program(inputs):
    with open("input.txt", "r") as data:
        # split string on commas, convert it to integers, store them in a list
        intcode = list(map(lambda x: int(x), data.read().split(",")))
        startIndex = 0
        while intcode[startIndex] != 99:
            # convert to string and pad 0s
            opcode_buffer = str(intcode[startIndex])
            while len(opcode_buffer) < 5:
                opcode_buffer = "0" + opcode_buffer

            print(f"OpCode Buffer: {opcode_buffer}")
            opcode = int(opcode_buffer[-2:])
            print(f"OpCode: {opcode}")

            if opcode == 1:
                # do addition
                if opcode_buffer[-3] == "0":
                    #print("v1 position mode")
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    #print("v1 immediate mode")
                    v1 = intcode[startIndex + 1]
                if opcode_buffer[-4] == "0":
                    v2 = intcode[intcode[startIndex + 2]]
                else:
                    v2 = intcode[startIndex + 2]
                destination = intcode[startIndex + 3]
                #print(f"Setting index {destination} to {v1 + v2}")
                intcode[destination] = v1 + v2
                # increment starting index
                startIndex += 4
            elif opcode == 2:
                # do multiplication
                if opcode_buffer[-3] == "0":
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    v1 = intcode[startIndex + 1]
                if opcode_buffer[-4] == "0":
                    v2 = intcode[intcode[startIndex + 2]]
                else:
                    v2 = intcode[startIndex + 2]
                destination = intcode[startIndex + 3]
                #print(f"Setting index {destination} to {v1 * v2}")
                intcode[destination] = v1 * v2
                # increment starting index
                startIndex += 4
            elif opcode == 3:
                # take input
                v1 = inputs.pop(0)
                #print(f"Setting index {intcode[startIndex + 1]} to {v1}")
                intcode[intcode[startIndex + 1]] = v1
                startIndex += 2
            elif opcode == 4:
                # print output
                if opcode_buffer[-3] == "0":
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    v1 = intcode[startIndex + 1]
                print(f"Output: {v1}")
                startIndex += 2
            elif opcode == 5:
                if opcode_buffer[-3] == "0":
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    v1 = intcode[startIndex + 1]
                if opcode_buffer[-4] == "0":
                    v2 = intcode[intcode[startIndex + 2]]
                else:
                    v2 = intcode[startIndex + 2]
                if v1 != 0:
                    startIndex = v2
                else:
                    startIndex += 3
            elif opcode == 6:
                if opcode_buffer[-3] == "0":
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    v1 = intcode[startIndex + 1]
                if opcode_buffer[-4] == "0":
                    v2 = intcode[intcode[startIndex + 2]]
                else:
                    v2 = intcode[startIndex + 2]
                if v1 == 0:
                    startIndex = v2
                else:
                    startIndex += 3
            elif opcode == 7:
                if opcode_buffer[-3] == "0":
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    v1 = intcode[startIndex + 1]
                if opcode_buffer[-4] == "0":
                    v2 = intcode[intcode[startIndex + 2]]
                else:
                    v2 = intcode[startIndex + 2]
                destination = intcode[startIndex + 3]
                if v1 < v2:
                    intcode[destination] = 1
                else:
                    intcode[destination] = 0
                startIndex += 4
            elif opcode == 8:
                if opcode_buffer[-3] == "0":
                    v1 = intcode[intcode[startIndex + 1]]
                else:
                    v1 = intcode[startIndex + 1]
                if opcode_buffer[-4] == "0":
                    v2 = intcode[intcode[startIndex + 2]]
                else:
                    v2 = intcode[startIndex + 2]
                destination = intcode[startIndex + 3]
                if v1 == v2:
                    intcode[destination] = 1
                else:
                    intcode[destination] = 0
                startIndex += 4
            else:
                print(f"Unknown Opcode: {opcode}")
                break



        return intcode[0]

print(run_program([5]))