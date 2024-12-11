import functools

test_ = "125 17"
input_ = open("input/input11.txt", "r").read()

stones = list(map(int, input_.split()))

@functools.lru_cache(maxsize=None)
def single_blink_stone(value):

    text = str(value)
    digits = len(text)
    
    if value == 0:
        return (1, None)
    elif digits % 2 == 0:
        mid = digits // 2
        num1 = int(text[:mid])
        num2 = int(text[mid:])
        return (num1, num2)
    else:
        return (value * 2024, None)

@functools.lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):
    
    left_stone, right_stone = single_blink_stone(stone)
    
    # last iteration
    if depth == 1:
        
        # count if one or two stones
        if right_stone is None:
            return 1
        else:
            return 2
    
    else:
        # recurse to next level and add stones if there are two
        output = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            output += count_stone_blinks(right_stone, depth - 1)
        
        return output
    

def run(count):
    output = 0
    
    # look at each stone
    for stone in stones:
        
        # how many stones does one turn into?
        output += count_stone_blinks(stone, count)
        
    return output

def main():
    
    out25 = run(25)
    out75 = run(75)
    
    print(f"Part 1: {out25}")
    print(f"Part 2: {out75}")
   
main()