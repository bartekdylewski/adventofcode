class Coord:
    def __repr__(self):
        return f"<{self.x}, {self.y}>"

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.in_bounds = 0 <= self.x < w and 0 <= self.y < h

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def apply_vector(self, v):
        dx, dy = v
        return Coord(self.x + dx, self.y + dy, self.w, self.h)

    # returns vector between self and other
    def diff(self, other):
        return (self.x - other.x, self.y - other.y)


def prepare_input(puzzle_input):
    lines = puzzle_input.splitlines()
    w = len(lines[0])
    h = len(lines)

    antennas = {}

    for y, row in enumerate(lines):
        for x, val in enumerate(row):
            if val != ".":
                if val not in antennas:
                    antennas[val] = []
                antennas[val].append(Coord(x, y, w, h))

    return (antennas, w, h)


def part_one(puzzle_input):
    antennas, w, h = puzzle_input

    antinodes = set()

    for antenna_type in antennas.keys():
        locs = antennas[antenna_type]

        # for every combination of locations, create a coord based on diff. If in bounds, add to list
        for a in locs:
            for b in locs:
                if a == b:
                    continue

                vector = a.diff(b)

                first = b.apply_vector([i * -1 for i in vector])
                second = a.apply_vector(vector)

                for v in [first, second]:
                    if v.in_bounds:
                        antinodes.add(v)

    return len(antinodes)


def part_two(puzzle_input):
    antennas, w, h = puzzle_input

    antinodes = set()

    for antenna_type in antennas.keys():
        locs = antennas[antenna_type]

        # for every combination of locations, create a coord based on diff. If in bounds, add to list
        # continue until both spawned vectors are out of bounds
        for a in locs:
            for b in locs:
                if a == b:
                    continue

                vector = a.diff(b)
                first, second = a, b

                while True:
                    first = first.apply_vector([i * -1 for i in vector])
                    second = second.apply_vector(vector)

                    if not first.in_bounds and not second.in_bounds:
                        break

                    for v in [first, second]:
                        if v.in_bounds:
                            antinodes.add(v)

    return len(antinodes)


puzzle_input = prepare_input(open("input/input8.txt", "r").read())
print(part_two(puzzle_input))