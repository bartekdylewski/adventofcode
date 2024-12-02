'''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
6 reports
5 levels

report is safe if both:
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

how many reports are safe?
'''

# testcases
# x = [7,6,4,2,1]
# y = [1,2,7,8,9]
# z = [1, 3, 2, 4, 5]
# all = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
# ]

file = "input2.txt"

def get_reports():
    reports = []
    with open(file, "r") as f:
        for line in f:
            report = line.strip().split()
            reports.append(report)
            # print(report)
        return reports

def isReportSafe(x):
    isSafe = True
    isIncreasing = None
    wasIncreasing = isIncreasing
    for i in range(len(x)-1):
        if 1 <= abs(int(x[i]) - int(x[i+1])) <= 3:
            if int(x[i]) < int(x[i+1]):
                isIncreasing = True
            elif int(x[i]) > int(x[i+1]):
                isIncreasing = False
            
            if i != 0 and wasIncreasing != isIncreasing:
                isSafe = False
                break
            wasIncreasing = isIncreasing
            
        else:
            isSafe = False
            break
    return isSafe

# for report in all:
#     print(isReportSafe(report))
    
def main():
    count = 0
    reports = get_reports()
    print(reports)
    for report in reports:
        if isReportSafe(report):
            count += 1
            
            
    
    for report in reports:
        print(report, isReportSafe(report))
    print(count)

main()
        