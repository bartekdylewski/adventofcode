directions = [
    (0, 1),   # Prawo
    (0, -1),  # Lewo
    (1, 0),   # Dół
    (-1, 0),  # Góra
    (1, 1),   # Na skos w dół w prawo
    (1, -1),  # Na skos w dół w lewo
    (-1, 1),  # Na skos w górę w prawo
    (-1, -1)  # Na skos w górę w lewo
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


def main():
    choose = int(input("1 for test, 2 for input: "))
    if choose == 1:
        list = string_to_list(get_test())
    elif choose == 2:
        list = string_to_list(get_input())
    
    choose = int(input("1 for part1, 2 for part2: "))
    if choose == 1:
        word = "XMAS"
        occurrences = count_word(list, word)
        print(f"Number of '{word}' occurencies: {occurrences}")
    elif choose == 2:
        
        pass

main()