import re

filename = 'day3/input.txt'
input = ''
with open(filename) as f:
    input = f.read().strip()

def calc(string):
    muls = re.findall('mul\(\d{1,3}\,\d{1,3}\)', string)

    total = 0
    for mul in muls:
        a, b = map(int, mul[4:-1].split(','))
        total += a*b

    return total

def part1():
    print(calc(input))
    
def part2():
    donts = input.split("don't()")
    total = calc(donts[0])
    for dont in donts[1:]:
        dos = dont.split("do()")
        for do in dos[1:]:
            total += calc(do)
    print(total)

part2()