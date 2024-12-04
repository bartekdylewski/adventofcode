directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Diagonally down-right
    (1, -1),  # Diagonally down-left
    (-1, 1),  # Diagonally up-right
    (-1, -1)  # Diagonally up-left
]
diagonals = [
    (1, 1),   # Down-right
    (1, -1),  # Down-left
    (-1, 1),  # Up-right
    (-1, -1)  # Up-left
]

def get_test():
    with open("test4.txt", "r") as f:
        return f.read()

def get_input():
    with open("input4.txt", "r") as f:
        return f.read()

def string_to_list(string):
    lines = string.split("\n")
    empty_char = "."
    rows = len(lines)
    cols = max(len(line) for line in lines)  # max chars in line
    final = [["" for _ in range(cols)] for _ in range(rows)]  # empty 2d matrix

    # fill matrix with characters
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            final[i][j] = char
    
    for i in range(len(final)):
        final[i] = [empty_char] + final[i] + [empty_char]
    
    # add lines of empty on top
    width = len(final[0])
    top_bottom = [empty_char] * width
    final.insert(0, top_bottom)
    final.append(top_bottom)

    return final

# find word in given direction
def find_word(matrix, word, start_row, start_col, direction):
    rows = len(matrix)
    cols = len(matrix[0])
    row, col = start_row, start_col
    
    for char in word:
        # if out of bounds or not equal to char, return False
        if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] != char:
            return False
        # move in direction
        row += direction[0]
        col += direction[1]
    return True

def count_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    
    for row in range(rows):
        for col in range(cols):
            # check if letter is the first letter of the word
            if matrix[row][col] == word[0]:
                # check 8 directions
                for direction in directions:
                    if find_word(matrix, word, row, col, direction):
                        count += 1
    return count

def count_x_with_words(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    
    # possible words for X
    valid_words = {"MAS", "SAM"}
    
    # check for every "A" in the matrix
    for row in range(1, rows - 1):  # dont check edges
        for col in range(1, cols - 1):
            if matrix[row][col] == "A":
                # get letters diagonal to A
                top_left = matrix[row - 1][col - 1]
                top_right = matrix[row - 1][col + 1]
                bottom_left = matrix[row + 1][col - 1]
                bottom_right = matrix[row + 1][col + 1]
                
                # create 2 full diagonals
                diagonal1 = top_left + "A" + bottom_right
                diagonal2 = top_right + "A" + bottom_left
                
                # check if diagonals are correct
                if diagonal1 in valid_words and diagonal2 in valid_words:
                    count += 1
    
    return count
    
def main():
    choose = int(input("1 for test, 2 for input: "))
    if choose == 1:
        matrix = string_to_list(get_test())
    elif choose == 2:
        matrix = string_to_list(get_input())
    
    choose = int(input("1 for part1, 2 for part2: "))
    if choose == 1:
        print(count_word(matrix, "XMAS"))
    elif choose == 2:
        print(count_x_with_words(matrix))

main()