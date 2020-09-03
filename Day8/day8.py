import numpy as np
from PIL import Image


def decode_image_input():
    with open("input", "r") as data:
        text = list(data.read())
        layers = []
        while len(text) > 0:
            layer = []
            for y in range(0, 6):
                l = []
                for x in range(0, 25):
                    l.append(text.pop(0))
                layer.append(l)
            layers.append(layer)

        return layers

def part1():
    layers = decode_image_input()

    # find fewest 0s
    current_best_value = -1
    current_best_index = -1
    for index, layer in enumerate(layers):
        zero_count = 0
        for l in layer:
            for i in l:
                if i == '0':
                    zero_count += 1
        if zero_count < current_best_value or current_best_value == -1:
            current_best_value = zero_count
            current_best_index = index

    # count 1 and 2, then multiply
    one_count = 0
    two_count = 0
    for l in layers[current_best_index]:
        for i in l:
            if i == '1':
                one_count += 1
            elif i == '2':
                two_count += 1

    print(one_count * two_count)


def part2():
    layers = decode_image_input()
    image_data = np.zeros([6, 25, 3], dtype=np.uint8)

    for y in range(0, 6):
        for x in range(0, 25):
            for l in layers:
                print(f"{x}, {y} : {l}")
                if l[y][x] == '0':
                    image_data[y][x] = [0, 0, 0]
                    break
                elif l[y][x] == '1':
                    image_data[y][x] = [255, 255, 255]
                    break

    img = Image.fromarray(image_data)
    img.save('day8.png')

#part1()
part2()
