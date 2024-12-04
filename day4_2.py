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
    
    # for i in range(len(final)):
    #     final[i] = [empty_char] + final[i] + [empty_char]
    
    # # add lines of empty on top
    # width = len(final[0])
    # top_bottom = [empty_char] * width
    # final.insert(0, top_bottom)
    # final.append(top_bottom)

    return final

def count_x_with_words(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    
    # Możliwe wzory dla X
    valid_words = {"MAS", "SAM"}
    
    # Sprawdź każde "A" w tablicy
    for row in range(1, rows - 1):  # Nie sprawdzamy krawędzi
        for col in range(1, cols - 1):
            if matrix[row][col] == "A":
                # Pobieramy litery na krzyż wokół "A"
                top_left = matrix[row - 1][col - 1]
                top_right = matrix[row - 1][col + 1]
                bottom_left = matrix[row + 1][col - 1]
                bottom_right = matrix[row + 1][col + 1]
                
                # Utwórz dwie przekątne
                diagonal1 = top_left + "A" + bottom_right
                diagonal2 = top_right + "A" + bottom_left
                
                # Sprawdź, czy przekątne są poprawnymi słowami
                if diagonal1 in valid_words and diagonal2 in valid_words:
                    count += 1
    
    return count

# Testowy input
matrix = string_to_list(get_input())

# Uruchomienie funkcji
result = count_x_with_words(matrix)
print(f"Number of X patterns found: {result}")
