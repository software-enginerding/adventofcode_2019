from re import findall


def extract_ints(line):
    return [int(x) for x in findall(r'-?\d+', line)]