import re

infile = 'day1/input.txt'

left = []
right = []

with open(infile, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = re.split('\s+', line.strip())
        left.append(int(line[0]))
        right.append(int(line[1]))

left.sort()
right.sort()

def part1(): 
    count = 0
    for i in range(0, len(left)):
        count += abs(left[i] - right[i])

    print(count)

def part2():
    total = 0
    for i in range(0, len(left)):
        total += left[i] * right.count(left[i])
            
    print(total)

part2()