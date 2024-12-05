from math import floor

# DELETE LAST EMPTY LINE IN INPUT FILE
def get_test():
    with open("test5.txt", "r") as f:
        return f.read()
def get_input():
    with open("input5.txt", "r") as f:
        return f.read()

"""
orders = [ [x,y], [x,y], [x,y], ...]
updates = [ [75,47,61,53,29],[97,61,53,29,13],[75,29,13], ... ]
"""
def split_order_update(string):
    orders, updates = [], []
    wasSpaced = False
    for line in string.split("\n"):
        if not wasSpaced:
            order = line.split("|")
            if line == "":
                wasSpaced = True
            orders.append(order)
        else:
            update = line.split(",")
            updates.append(update)
    orders.pop(-1)
    
    return orders, updates
    
def check_order(update, orders):
    for x, y in orders:  # for every rule x|y
        if x in update and y in update:  # check if both pages x and y are in update
            x_index = update.index(x)
            y_index = update.index(y)
            if x_index > y_index:  # if x is after y, return False, we violate the rule
                return False
    return True

def main():
    
    choose = int(input("1 for test, 2 for input: "))
    if choose == 1:
        data = get_test()
    elif choose == 2:
        data = get_input()
        
    orders, updates = split_order_update(data)
    orders = [[int(x), int(y)] for x, y in orders]
    updates = [[int(page) for page in update] for update in updates]
    
    print("Orders:")
    for order in orders:
        print(order)
    print("Updates:")
    for update in updates:
        print(update)
        
    choose = int(input("1 for part1, 2 for part2: "))
    if choose == 1:
        
        correct_updates = []
        for update in updates:
            if check_order(update, orders):
                correct_updates.append(update[len(update) // 2]) # middle page
        
        print(f"Correct updates middle pages: {correct_updates}")
        print(f"Sum of middle pages: {sum(correct_updates)}")
    elif choose == 2:
        pass

main()