import re

input = open("input/input13.txt").read().splitlines()
test = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279

""".strip().splitlines()

def parse(data):
    pattern = r"X\+(\d+), Y\+(\d+)|X=(\d+), Y=(\d+)"
    result = [[] for _ in range(data.count("") + 1)]
    machine = 0
    for i,element in enumerate(data):
        if element != "":
            matches = re.findall(pattern, element)
            # Flatten and filter out empty strings from the matches
            flattened = [int(x) for group in matches for x in group if x]
            a, b = flattened
            result[machine].append(a)
            result[machine].append(b)
        else:
            machine += 1
    return result

def calculate_cost(machine, max_moves=100):
    ax, ay , bx, by, px, py = machine
    cost = None
    min_cost = float('inf')
    isPossible = False
    
    for na in range(max_moves+1):
        for nb in range(max_moves+1):
            
            if ax*na + bx*nb == px and ay*na + by*nb == py: #TODO check
                isPossible = True
                cost = 3*na + nb
                min_cost = min(min_cost, cost)
    if isPossible:
        return min_cost
    else:
        return None

# Przykład
results = parse(input)
sum = 0
for element in results:
    if(calculate_cost(element)) != None:
        sum += calculate_cost(element)

print(f"{sum=}")

error = 10000000000000
sum2 = 0
for element in results:
    element[4] += error
    element[5] += error
    print(element)
    res = calculate_cost(element,999)
    if res != None:
        sum2 += res
        
print(f"{sum2=}")
