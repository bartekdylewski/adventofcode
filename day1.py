x, y = [], []
file = "input1.txt"

with open(file, "r") as f:
    for line in f:
        numbers = line.strip().split()
        left = int(numbers[0])
        right = int(numbers[1])
        x.append(left)
        y.append(right)


def sort(x, y):     
    x.sort()
    y.sort()

def distance_sum(x, y):
    sum = 0
    for i in range(len(x)):
        result = abs(x[i] - y[i])
        sum += result
    return sum

def similarity_score(x, y):
    sum = 0
    for i in range(len(x)):
        result = x[i] * y.count(x[i])
        sum += result
    return sum

def main():
    sort(x, y)
    print(distance_sum(x, y))
    print(similarity_score(x, y))
    
main()
