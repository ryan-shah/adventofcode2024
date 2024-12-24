infile = 'day2/input.txt'

reports = []

with open(infile) as f:
    for line in f:
        reports.append(line.strip().split(' '))

def part1():
    safe = 0
    for report in reports:
        prev_dir = int(report[0]) < int(report[1])
        is_safe = True
        for i in range(len(report) - 1): 
            curr = int(report[i])
            next = int(report[i+1])
            dir = (curr < next) == prev_dir
            prev_dir = curr < next
            diff = abs(curr - next)
            if not dir or diff > 3 or diff == 0:
                is_safe = False
                break
        # print(report, is_safe)
        if is_safe:
            safe += 1
    print(safe)

def check_safe(report):
    prev_dir = int(report[0]) < int(report[1])
    for i in range(len(report) - 1): 
        curr = int(report[i])
        next = int(report[i+1])
        dir = (curr < next) == prev_dir
        prev_dir = curr < next
        diff = abs(curr - next)
        if not dir or diff > 3 or diff == 0:
            return (i, False)
    # print(report, is_safe)
    return (0, True)

def part2():
    safe = 0
    for report in reports:
        index, is_safe = check_safe(report)
        if not is_safe:
            dup1 = report.copy()
            dup2 = report.copy()
            dup3 = report.copy()
            dup1.pop(index)
            dup2.pop(index-1)
            try:
                dup3.pop(index+1)
            except:
                pass
            is_safe = check_safe(dup1)[1] or check_safe(dup2)[1] or check_safe(dup3)[1]
        if is_safe:
            safe += 1
        #print(report, is_safe)
    print(safe)

part2()