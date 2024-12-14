from pathlib import Path

input_file = Path(__file__).parent.parent / "input" / "input14.txt"
input = input_file.read_text().splitlines()

input_map = [101, 103]
# input = open("input/input14.txt").read().splitlines()
test_map = [11,7]
test = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()

def parse(data):
    positions, velocities = [], []
    for line in data:
        pos, vel = line.split(" ") #split into p=x,y and v=x,y
        pos, vel = pos[2:], vel[2:] #delete p= and v=
        px, py = pos.split(",")
        vx, vy = vel.split(",")
        positions.append([int(px), int(py)])
        velocities.append((int(vx), int(vy)))
    return positions, velocities # lists of [x,y] for every robot

def move_all_once(positions, velocities, map_size):
    for i in range(len(positions)):
        positions[i][0] += velocities[i][0]
        positions[i][1] += velocities[i][1]
        
        # teleport if beyond map
        for j in range(2):
            if positions[i][j] >= map_size[j] or positions[i][j] < 0:
                positions[i][j] = positions[i][j] % map_size[j]
                
def visualize(positions, map_size):
    map = [["." for i in range(map_size[0])] for j in range(map_size[1])]
    for pos in positions:
        map[pos[1]][pos[0]] = "#"
    for row in map:
        print("".join(row))
    print("\n")
    
def find_quadrants(positions, map_size):
    divider_x = map_size[0] // 2
    divider_y = map_size[1] // 2
    quadrants = [] # what quadrant is each robot in 
    # 12
    # 34    0 if in line with divider
    for x,y in positions:
        if x == divider_x or y == divider_y:
            quadrants.append(0)
        elif x < divider_x and y < divider_y:
            quadrants.append(1)
        elif x > divider_x and y < divider_y:
            quadrants.append(2)
        elif x < divider_x and y > divider_y:
            quadrants.append(3)
        elif x > divider_x and y > divider_y:
            quadrants.append(4)
        else:
            print("ERROR in quadrants calssification")
    return quadrants

def find_safety_factor(quadrants):
    # find how much robots in each quadrant
    robots_in_quadrant = [0,0,0,0,0] # 0,1,2,3,4
    for i in range(len(quadrants)):
        robots_in_quadrant[quadrants[i]] += 1
    safety_factor = 1
    for i in range(1,5):
        safety_factor *= robots_in_quadrant[i]
    return safety_factor

def check_for_tree(positions, map, time):
    for pos in positions:
        if positions.count(pos) > 1:
            return False
    visualize(positions, map)
    print(f"CHRISTMAS TREE FOUND at {time+1} seconds")
    return True
    
def main():
    # data = test, test_map
    data = input, input_map

    pos, vel = parse(data[0])
    # print(pos)
    for i in range(9999):
        move_all_once(pos, vel, data[1])
        # visualize(pos, data[1])
        check_for_tree(pos, data[1],i)
    quadrants = find_quadrants(pos, data[1])
    safety_factor = find_safety_factor(quadrants)
    print(safety_factor)
    
main()