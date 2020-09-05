from intcode_computer import IntcodeComputer
from enum import Enum
import numpy as np
from PIL import Image


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Robot:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.direction = Direction.UP

    def turn_right(self):
        if self.direction == Direction.UP:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN:
            self.direction = Direction.LEFT
        else:
            self.direction = Direction.UP

    def turn_left(self):
        if self.direction == Direction.UP:
            self.direction = Direction.LEFT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.UP
        elif self.direction == Direction.DOWN:
            self.direction = Direction.RIGHT
        else:
            self.direction = Direction.DOWN

    def move(self):
        if self.direction == Direction.UP:
            self.x += 1
        elif self.direction == Direction.RIGHT:
            self.y += 1
        elif self.direction == Direction.DOWN:
            self.x = self.x - 1
        else:
            self.y = self.y - 1


def part1():
    with open("input", "r") as data:
        text = data.read()
        computer = IntcodeComputer(data=text)
        tiles = {}
        robot = Robot()
        while computer.is_halted is not True:
            current_color = tiles.get(f"{robot.x},{robot.y}", 0)
            new_color = computer.run_program([current_color])
            print(f"New Color: {new_color}")
            if new_color is None:
                break
            # save current color
            tiles[f"{robot.x},{robot.y}"] = new_color
            to_turn = computer.run_program([])
            if to_turn == 0:
                robot.turn_left()
            else:
                robot.turn_right()
            robot.move()

        print(len(tiles.keys()))


def part2():
    with open("input", "r") as data:
        text = data.read()
        computer = IntcodeComputer(data=text)
        # Start on White Square
        tiles = {"250,250": 1}
        robot = Robot(250, 250)
        image_data = np.zeros([500, 500, 3], dtype=np.uint8)
        image_data[robot.y][robot.x] = [255, 255, 255]
        while computer.is_halted is not True:
            current_color = tiles.get(f"{robot.x},{robot.y}", 0)
            new_color = computer.run_program([current_color])
            print(f"New Color: {new_color}")
            if new_color is None:
                break
            # save current color
            tiles[f"{robot.x},{robot.y}"] = new_color
            if new_color == 0:
                image_data[robot.y][robot.x] = [0, 0, 0]
            else:
                image_data[robot.y][robot.x] = [255, 255, 255]
            to_turn = computer.run_program([])
            if to_turn == 0:
                robot.turn_left()
            else:
                robot.turn_right()
            robot.move()

        img = Image.fromarray(image_data)
        img.save('day11.png')


part2()