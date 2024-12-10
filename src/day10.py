test = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
input = open("input/input10.txt").read().strip()

DIRECTIONS = [(0,1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

def string_to_matrix(string):
    """
    matrix[y][x], y is the row (top-down), x is the column (left-right)
    """
    matrix = []
    for line in string.split("\n"):
        if line:
            matrix.append([int(x) for x in line])
    return matrix

def find_bases(matrix):
    bases = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == 0:
                bases.append((y, x))
    return bases

def dfs(y, x, visited, matrix):
    """Depth First Search (Recurrent) function to look for paths 0 -> 9"""

    if (y, x) in visited:
        return set() # If we have already visited this cell, return an empty set
    
    visited.add((y, x)) # Mark the cell as visited
    # print(f"Visiting ({y}, {x}), value: {matrix[y][x]}")

    if matrix[y][x] == 9: # If we have reached the peak, return the peak
        # print(f"Found peak at ({y}, {x})")
        return {(y, x)}
    
    peaks = set() # Set of peaks found in the DFS
    for dy, dx in DIRECTIONS:
        ny, nx = y+dy, x+dx
        # check if the next cell is within the matrix and if the value of the next cell is the current value + 1
        if 0 <= ny < len(matrix) and 0 <= nx < len(matrix[0]) and matrix[ny][nx] - matrix[y][x] == 1:
            peaks |= dfs(ny, nx, visited, matrix) # Union of the peaks found in the next cell (connect)

    return peaks

def main():
    matrix = string_to_matrix(test)
    bases = find_bases(matrix)

    # PART 1: Liczba szczytów (tylko dla bazy)
    total_score = 0
    for y, x in bases:
        visited = set()
        peaks = dfs(y, x, visited, matrix)
        total_score += len(peaks)  # Liczymy liczbę szczytów
    print("PART 1 TOTAL SCORE:", total_score)

    # PART 2: i dont know how to do distinct paths.

main()