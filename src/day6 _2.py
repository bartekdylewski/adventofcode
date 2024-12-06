from collections import deque
import time  # Import the time module for timing

# Movements in four directions
DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
TURN_ORDER = ["^", ">", "v", "<"]

def parse_input(input_str):
    """
    Parses the input string into a 2D list (matrix).
    """
    return [list(line) for line in input_str.splitlines()]

def add_border(matrix, border_char='F'):
    """
    Adds a border around the matrix with the specified character.
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    bordered_matrix = [[border_char] * (cols + 2)]  # Top border
    for row in matrix:
        bordered_matrix.append([border_char] + row + [border_char])  # Left and right borders
    bordered_matrix.append([border_char] * (cols + 2))  # Bottom border
    
    return bordered_matrix

def simulate_guard(matrix, start_pos, wall_pos=None):
    """
    Simulates the guard's movement starting from `start_pos`.
    Optionally places a wall at `wall_pos`.
    Returns True if the guard falls into an infinite loop.
    """
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    i, j, direction = start_pos
    if wall_pos:
        matrix[wall_pos[0]][wall_pos[1]] = "#"

    while True:
        # Track the current state (position and direction)
        state = (i, j, direction)
        if state in visited:
            return True  # Loop detected
        visited.add(state)

        di, dj = DIRECTIONS[direction]
        ni, nj = i + di, j + dj

        if matrix[ni][nj] == "F":  # Reached the goal
            return False
        if matrix[ni][nj] == "#":  # Turn right on obstacle
            current_index = TURN_ORDER.index(direction)
            direction = TURN_ORDER[(current_index + 1) % 4]
        else:
            # Move to the next position
            i, j = ni, nj

def find_all_loop_positions(matrix):
    """
    Finds all positions where placing a wall causes the guard to enter an infinite loop.
    """
    rows, cols = len(matrix), len(matrix[0])
    # Locate the starting position of the guard
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] in DIRECTIONS:
                start_pos = (i, j, matrix[i][j])

    loop_positions = 0

    # Check every possible position for placing a wall
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == ".":  # Only consider empty spaces
                if simulate_guard([row[:] for row in matrix], start_pos, wall_pos=(i, j)):
                    loop_positions += 1

    return loop_positions

def main():
    """
    Main function to execute the logic.
    Reads the input, processes the matrix, and computes the result.
    """
    with open("input/input6.txt", "r") as f:
        input_data = f.read().strip()

    matrix = parse_input(input_data)
    matrix = add_border(matrix)  # Add a border for safety

    start_time = time.time()  # Start timing
    result = find_all_loop_positions(matrix)
    end_time = time.time()  # End timing

    print("NUMBER OF LOOP POSITIONS:", result)
    print(f"Execution Time: {end_time - start_time:.2f} seconds")  # Print the elapsed time

main()
