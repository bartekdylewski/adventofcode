from pathlib import Path

input = open(Path(__file__).parent.parent / "input" / "input15.txt").read()
test = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

DIRECTIONS = {
    "v": [0, 1],
    "^": [0, -1],
    "<": [-1, 0],
    ">": [1, 0],
}


class Warehouse:
    def __init__(self, data):
        self.data = data
        self.walls = []
        self.boxes = []
        self.robot = []
        self.moves = []
        self.map_len = 0

    def parse(self):
        map_, moves = self.data.split("\n\n")
        self.map_len = len(map_.splitlines()[0])+10
        for y, row in enumerate(map_.splitlines()):
            y = y - 1
            for x, char in enumerate(row):
                if char == "#":
                    self.walls.append([x, y])
                elif char == "O":
                    self.boxes.append([x, y])
                elif char == "@":
                    self.robot.append(x)
                    self.robot.append(y)
        

        self.moves = "".join(moves.split("\n"))

    def visualize(self):
        map_ = [["." for _ in range(self.map_len)] for _ in range(self.map_len)]
        for pos in self.walls:
            map_[pos[1]][pos[0]] = "#"
        for pos in self.boxes:
            map_[pos[1]][pos[0]] = "O"
        rx, ry = self.robot
        map_[ry][rx] = "@"
        for row in map_:
            print("".join(row))
        print(f"Robot at: {self.robot}")

    def show_moves(self):
        print(self.moves)

    def move(self, direction):
        vx, vy = DIRECTIONS[direction]
        rx, ry = self.robot

        # Następna pozycja, w którą chce wejść robot
        next_pos = [rx + vx, ry + vy]

        # Jeśli następna pozycja to ściana, nic nie rób
        if next_pos in self.walls:
            return

        # Jeśli następna pozycja to skrzynia
        if next_pos in self.boxes:
            current_pos = next_pos
            positions_to_update = []  # Lista par: (stara_pozycja, nowa_pozycja)

            # Sprawdzanie skrzyń w linii
            while current_pos in self.boxes:
                next_next_pos = [current_pos[0] + vx, current_pos[1] + vy]

                if next_next_pos in self.walls:
                    # Jeśli za skrzynią jest ściana, anuluj ruch
                    return
                elif next_next_pos in self.boxes:
                    # Jeśli za skrzynią jest inna skrzynia, kontynuuj
                    positions_to_update.append((current_pos, next_next_pos))
                    current_pos = next_next_pos
                else:
                    # Jeśli za skrzynią jest wolne miejsce, dodaj i przerwij pętlę
                    positions_to_update.append((current_pos, next_next_pos))
                    break

            # Przesuń wszystkie skrzynie, jeśli wszystkie ruchy są możliwe
            for old_pos, new_pos in reversed(positions_to_update):
                self.boxes[self.boxes.index(old_pos)] = new_pos

            # Przesuń robota na miejsce pierwszej skrzyni
            self.robot = next_pos

        else:
            # Jeśli następna pozycja jest wolna, przesuń robota
            self.robot = next_pos

    def calculate_gps_sum(self):
        total = 0
        for x, y in self.boxes:
            gps = (100 * y) + x  # Odległość od górnej i lewej krawędzi
            total += gps
        return total


def main():
    warehouse = Warehouse(input)
    warehouse.parse()
    warehouse.visualize()

    moves = warehouse.moves
    for i in range(len(moves)):
        # print(f"Move {moves[i]}")
        warehouse.move(moves[i])
        # warehouse.visualize()
    warehouse.visualize()

    gps_sum = warehouse.calculate_gps_sum()
    print(f"Sum of GPS coordinates: {gps_sum}")


main()
