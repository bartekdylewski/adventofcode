def get_test():
    with open("test/test6.txt", "r") as f:
        return f.read().rstrip()

def get_input():
    with open("input/input6.txt", "r") as f:
        return f.read().rstrip()

def add_border(matrix, border_char='F'):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    bordered_matrix = [[border_char] * (cols + 2)]  # Top border
    for row in matrix:
        bordered_matrix.append([border_char] + row + [border_char])  # Side borders
    bordered_matrix.append([border_char] * (cols + 2))  # Bottom border

    return bordered_matrix

def get_matrix(string):
    return [list(line) for line in string.split("\n")]

# Ruchy w czterech kierunkach
DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
TURN_ORDER = ["^", ">", "v", "<"]

def move_guard(matrix):
    rows, cols = len(matrix), len(matrix[0])
    guard_found = False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] in DIRECTIONS:  # found guard
                guard_found = True
                direction = matrix[i][j]
                di, dj = DIRECTIONS[direction] # get direction by key = ex. ^
                ni, nj = i + di, j + dj  # set new pos of guard

                if matrix[ni][nj] == "F":  # end
                    matrix[i][j] = "C"
                    matrix[ni][nj] = direction
                    return True

                if matrix[ni][nj] == "#":  # hits a wall, change direction
                    current_index = TURN_ORDER.index(direction)
                    new_direction = TURN_ORDER[(current_index + 1) % 4]
                    matrix[i][j] = new_direction
                else:  # move guard
                    matrix[i][j] = "C"
                    matrix[ni][nj] = direction
                    
                return False

    if not guard_found:  # if no guard -> end
        return True

def count_checked_spaces(matrix):
    return sum(row.count("C") for row in matrix)

def main():
    string = get_input()
    matrix = get_matrix(string)
    matrix = add_border(matrix)

    while not move_guard(matrix):
        pass  # simulate guard movement

    print("FINAL MATRIX:")
    for row in matrix:
        print("".join(row))

    print("CHECKED SPACES:", count_checked_spaces(matrix))

main()
