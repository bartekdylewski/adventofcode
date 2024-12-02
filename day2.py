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

all = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

file = "input2.txt"

def get_reports(file):
    """
    Get reports from file.
    """
    reports = []
    with open(file, "r") as f:
        for line in f:
            report = line.strip().split()
            reports.append(report)
            # print(report)
        return reports

def isReportSafe(x):
    """
    Check if the report is safe or not.
    """
    dampener = 0
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
    
def canBecomeSafe(report):
    """
    Check if a report can become safe by removing only one level.
    """
    for i in range(len(report)):
        # new list without report[i]
        modified_report = report[:i] + report[i+1:]
        if isReportSafe(modified_report):
            return True
    return False

def main():
    count = 0
    reports = get_reports(file)
    for report in reports:
        safe = isReportSafe(report)
        fixable = canBecomeSafe(report)
        print(f"safe: {safe:1} fixable: {fixable:1} report: {report}")
        if safe:
            count += 1
        else:
            if fixable:
                count += 1
    print(count)

main()
        