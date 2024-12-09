def parse_to_blocks(disk_map):
    """
    Converts the input disk map to a list of blocks where:
    - Numbers represent file IDs.
    - Dots (.) represent free space.
    """
    blocks = []
    file_id = 0  # Starting file ID

    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])  # Length of the file
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0  # Free space
        blocks.extend([str(file_id)] * file_length)  # Add file blocks
        blocks.extend(['.'] * free_length)           # Add free space blocks
        file_id += 1
        i += 2  # Move to the next pair

    return blocks

def visualize_blocks(blocks):
    """
    Joins the list of blocks into a string for visualization.
    """
    return ''.join(blocks)

# def move_files(blocks):
#     """
#     Move files to the leftmost span of free space blocks that could fit the file.
#     """
#     file_positions = {}
#     free_spaces = []

#     # Identify positions of files and free spaces
#     for i, block in enumerate(blocks):
#         if block != '.':
#             if block not in file_positions:
#                 file_positions[block] = []
#             file_positions[block].append(i)
#         else:
#             free_spaces.append(i)

#     # Sort files by file ID in descending order
#     sorted_files = sorted(file_positions.keys(), key=int, reverse=True)

#     for file_id in sorted_files:
#         positions = file_positions[file_id]
#         file_length = len(positions)

#         # Find the leftmost span of free space that can fit the file
#         for start in range(len(free_spaces) - file_length + 1):
#             if free_spaces[start + file_length - 1] - free_spaces[start] == file_length - 1:
#                 # Move the file to the free space
#                 for i in range(file_length):
#                     blocks[free_spaces[start + i]] = file_id
#                     blocks[positions[i]] = '.'
#                 # Update free spaces
#                 free_spaces = [pos for pos in free_spaces if pos < free_spaces[start] or pos > free_spaces[start + file_length - 1]]
#                 break

#     return blocks

def checksum(blocks):
    """
    Calculate the checksum by summing the position of the file multiplied by its ID.
    """
    sum = 0
    for i, block in enumerate(blocks):
        if block != '.':
            sum += i * int(block)

    return sum

def compact_blocks(blocks):
    """
    This function compresses the blocks by moving all files to the right, eliminating gaps.
    """
    left = 0
    right = len(blocks) - 1
    
    while left < right:
        # Move right pointer to find a file
        while right >= 0 and blocks[right] == '.':
            right -= 1
        
        # Move left pointer to find a free space
        while left < len(blocks) and blocks[left] != '.':
            left += 1

        if left < right:
            # Swap the file with free space
            blocks[left], blocks[right] = blocks[right], blocks[left]
            left += 1
            right -= 1
    
    return blocks

# Example usage
# input_line = "2333133121414131402"  # Test input string
input_line = open("input/input9.txt").read().strip()  # Read the input file

# Convert the input string to blocks
blocks = parse_to_blocks(input_line)

# Part1: Initial state before file movement (compact and visualize the blocks)
blocks1 = blocks.copy()  # Make a copy before compact_blocks
blocks1 = compact_blocks(blocks1)
print("Part1: Before moving files")
print(visualize_blocks(blocks1))
print("Part1 checksum:", checksum(blocks1))

# # Part2: Move files to the leftmost span of free space blocks
# blocks2 = move_files(blocks)
# print("Part2: After moving files")
# print(visualize_blocks(blocks2))
# print("Part2 checksum:", checksum(blocks2))

