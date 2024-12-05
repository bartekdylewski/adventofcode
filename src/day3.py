import re

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def get_memory(file):
    with open(file, "r") as f:
        memory = f.read()
        return memory

def multiply(x, y):
    """
    Multiplies if x and y are within the range of 0 to 999
    """
    if( 0 <= x <= 999 and 0 <= y <= 999):
        return x * y
    else:
        return ValueError("x and y must be within the range of 0 to 999")

def get_values(element:str):
    """
    Returns the values of the element in syntas mul(x,y)
    """
    values = element[4:-1]
    x, y = values.split(",")
    return int(x), int(y)

def main():
    memory = get_memory("input/input3.txt") # get string from file
    
    # "mul" finds mul
    # \( and \) finds the braces
    # \d{1,3} finds any 1-3 digit number
    regex_mul_do_dont = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    action_list = re.findall(regex_mul_do_dont, memory) # find actions
    
    # True = always multiplies
    # False = only multiplies when "do()" is active
    alwaysMul = int(input("Always multiply? 1 for yes, 0 for no: "))
    showActions = int(input("Show list of actions? 1 for yes, 0 for no: "))
    
    sum = 0
    state = True
    for element in action_list:
        if element == "do()":
            state = True
        elif element == "don't()":
            state = False
        else:
            x, y = get_values(element)
            if state or alwaysMul:
                sum += multiply(x, y)
    if showActions: print(action_list)
    print(sum)
    
main()