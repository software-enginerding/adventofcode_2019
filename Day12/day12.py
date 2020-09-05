from itertools import combinations
from collections import defaultdict

# <x=1, y=-4, z=3>
# <x=-14, y=9, z=-4>
# <x=-4, y=-6, z=7>
# <x=6, y=-9, z=-11>


def compute_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0
        self.start_x = x
        self.start_y = y
        self.start_z = z

    def apply_gravity(self, other):
        if isinstance(other, Moon):
            if self.x > other.x:
                self.vel_x -= 1
                other.vel_x += 1
            elif self.x < other.x:
                self.vel_x += 1
                other.vel_x -= 1
            if self.y > other.y:
                self.vel_y -= 1
                other.vel_y += 1
            elif self.y < other.y:
                self.vel_y += 1
                other.vel_y -= 1
            if self.z > other.z:
                self.vel_z -= 1
                other.vel_z += 1
            elif self.z < other.z:
                self.vel_z += 1
                other.vel_z -= 1

    def apply_velocity(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.z += self.vel_z

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def has_no_velocity(self):
        return self.vel_x == 0 and self.vel_y == 0 and self.vel_z == 0

    def is_in_starting_position(self):
        return self.x == self.start_x and self.y == self.start_y and self.z == self.start_z

    def is_in_starting_x_position(self):
        return self.x == self.start_x and self.vel_x == 0

    def is_in_starting_y_position(self):
        return self.y == self.start_y and self.vel_y == 0

    def is_in_starting_z_position(self):
        return self.z == self.start_z and self.vel_z == 0

    def get_axis_value(self, axis_index):
        if axis_index == 0:
            return self.x
        elif axis_index == 1:
            return self.y
        else:
            return self.z

    def get_axis_velocity_value(self, axis_index):
        if axis_index == 0:
            return self.vel_x
        elif axis_index == 1:
            return self.vel_y
        else:
            return self.vel_z

    def __hash__(self):
        return hash((self.x, self.y, self.z,self.vel_x, self.vel_y, self.vel_z))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Pos({self.x}, {self.y}, {self.z}) Vel({self.vel_x}, {self.vel_y}, {self.vel_z})"


def part1():
    moons = []
    with open("input", "r") as data:
        for line in data.readlines():
            coords = list(map(lambda s: int(s.split("=")[1]), line.strip("\n").replace(">", "").split(",")))
            moons.append(Moon(coords[0], coords[1], coords[2]))

    pairs = list(combinations(moons, 2))

    print(moons)
    for i in range(0, 1000):
        for p in pairs:
            p[0].apply_gravity(p[1])

        for m in moons:
            m.apply_velocity()

    system_energy = 0
    for m in moons:
        system_energy += m.total_energy()

    print(system_energy)


# each axis cycles independently of the others. Find the period for each axis then for the LCM of all the periods
def part2():
    moons = []
    with open("input", "r") as data:
        for line in data.readlines():
            coords = list(map(lambda s: int(s.split("=")[1]), line.strip("\n").replace(">", "").split(",")))
            moons.append(Moon(coords[0], coords[1], coords[2]))

    pairs = list(combinations(moons, 2))
    # x y and z axis cycles
    cycles = [0, 0, 0]
    # current tick
    count = 0
    # dictionary of previous states
    seen = defaultdict(set)
    while 0 in cycles:
        for p in pairs:
            p[0].apply_gravity(p[1])

        for m in moons:
            m.apply_velocity()

        # loop over each axis
        for i in range(3):
            # skip if this axis has been found
            if cycles[i] != 0:
                continue
            # account for position and velocity
            state = []
            for m in moons:
                state.append(m.get_axis_value(i))
                state.append(m.get_axis_velocity_value(i))
            # string is hashable
            state_str = str(state)
            if state_str in seen[i]:
                cycles[i] = count
                print(f"Setting {i} to {count}")
            else:
                seen[i].add(state_str)

        count += 1

    print(cycles)
    print(compute_lcm(cycles[0], compute_lcm(cycles[1], cycles[2])))



part2()