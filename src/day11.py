test_ = "125 17".split()
input_ = open("input/input11.txt").read().strip().split()

def int_list(list):
    return [int(i) for i in list]

def blink(list):
    new_list = []
    for stone in list:
        # if s == 0, replace by s == 1
        # if even digits, split stone in halves
        # else s *= 2024
        digits = len(str(stone))
        # print(digits)
        
        if int(stone) == 0:
            new_list.append(1)
        elif digits % 2 == 0:
            mid = digits // 2
            num1 = str(stone)[:mid]
            num2 = str(stone)[mid:]
            # print(f" {num1=} {num2=}")
            new_list.append(int(num1))
            new_list.append(int(num2))
        else:
            new_list.append(int(stone) * 2024)
            
    return new_list

def main():
    list = int_list(test_)
    print("0 : ",list)
    current = list
    for i in range(1,76):
        current = blink(current)
        # print(i,": ",current)
        print(i, len(current))
    print("len(blink25)= ",len(current))
    # 50min for part1
    
main()