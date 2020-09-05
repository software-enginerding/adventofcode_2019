class IntcodeComputer:
    def __init__(self, data: str, phase: int = None):
        # split string on commas, convert it to integers, store them in a list
        self.intcode = { i: v for i, v in enumerate(list(map(lambda x: int(x), data.split(","))))}
        self.remaining_inputs = [phase] if phase is not None else []
        self.start_index = 0
        self.relative_base = 0
        self.is_halted = False


    def run_program(self, inputs):
        self.remaining_inputs = self.remaining_inputs + inputs
        while self.intcode[self.start_index] != 99:
            # convert to string and pad 0s
            opcode_buffer = str(self.intcode[self.start_index])
            while len(opcode_buffer) < 5:
                opcode_buffer = "0" + opcode_buffer

            opcode = int(opcode_buffer[-2:])

            if opcode == 1:
                # do addition
                v1 = self.get_value(opcode_buffer, 0)
                v2 = self.get_value(opcode_buffer, 1)
                destination = self.get_value_index(opcode_buffer, 2)
                self.intcode[destination] = v1 + v2
                # increment starting index
                self.start_index += 4
            elif opcode == 2:
                # do multiplication
                v1 = self.get_value(opcode_buffer, 0)
                v2 = self.get_value(opcode_buffer, 1)
                destination = self.get_value_index(opcode_buffer, 2)
                self.intcode[destination] = v1 * v2
                # increment starting index
                self.start_index += 4
            elif opcode == 3:
                # take input
                v1 = self.remaining_inputs.pop(0)
                destination = self.get_value_index(opcode_buffer, 0)
                self.intcode[destination] = v1
                self.start_index += 2
            elif opcode == 4:
                # print output
                v1 = self.get_value(opcode_buffer, 0)
                last_output = v1
                self.start_index += 2
                return last_output
            elif opcode == 5:
                v1 = self.get_value(opcode_buffer, 0)
                v2 = self.get_value(opcode_buffer, 1)
                if v1 != 0:
                    self.start_index = v2
                else:
                    self.start_index += 3
            elif opcode == 6:
                v1 = self.get_value(opcode_buffer, 0)
                v2 = self.get_value(opcode_buffer, 1)
                if v1 == 0:
                    self.start_index = v2
                else:
                    self.start_index += 3
            elif opcode == 7:
                v1 = self.get_value(opcode_buffer, 0)
                v2 = self.get_value(opcode_buffer, 1)
                destination = self.get_value_index(opcode_buffer, 2)
                if v1 < v2:
                    self.intcode[destination] = 1
                else:
                    self.intcode[destination] = 0
                self.start_index += 4
            elif opcode == 8:
                v1 = self.get_value(opcode_buffer, 0)
                v2 = self.get_value(opcode_buffer, 1)
                destination = self.get_value_index(opcode_buffer, 2)
                if v1 == v2:
                    self.intcode[destination] = 1
                else:
                    self.intcode[destination] = 0
                self.start_index += 4
            elif opcode == 99:
                print("halting")
                self.is_halted = True
                return None
            elif opcode == 9:
                self.relative_base += self.get_value(opcode_buffer, 0)
                self.start_index += 2
            else:
                break

    def get_value(self, opcode_buffer, parameter_index):
        return self.intcode.get(self.get_value_index(opcode_buffer, parameter_index), 0)

    def get_value_index(self, opcode_buffer, parameter_index):
        if parameter_index == 0:
            buffer_index, start_index_offset = -3, 1
        elif parameter_index == 1:
            buffer_index, start_index_offset = -4, 2
        else:
            buffer_index, start_index_offset = -5, 3

        if opcode_buffer[buffer_index] == "0":
            return self.intcode.get(self.start_index + start_index_offset, 0)
        elif opcode_buffer[buffer_index] == "1":
            return self.start_index + start_index_offset
        else:
            return self.intcode.get(self.start_index + start_index_offset, 0) + self.relative_base


