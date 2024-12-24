import re

prompt = []

with open('day4/input.txt') as file:
    for line in file:
        prompt.append(line.strip())

def find_words(line):
    count = len(re.findall('XMAS', line))
    count += len(re.findall('SAMX', line))
    return count

def find_words_horizontal(lines):
    count = 0
    for line in lines:
        count += find_words(line)
    return count

def find_words_vertical(lines):
    count = 0
    for i in range(len(lines[0])):
        line = ''
        for j in range(len(lines)):
            line += lines[j][i]
        count += find_words(line)
        # print(line)
    return count

def find_words_diagonal(lines):
    count = 0
    for i in range(len(lines)):
        line = ''
        for j in range(len(lines[0])):
            if i+j < len(lines):
                line += lines[i+j][j]
        count += find_words(line)
    for i in range(1, len(lines)):
        line = ''
        for j in range(len(lines[0])):
            if j+i < len(lines):
                line += lines[j][j+i]
        count += find_words(line)
    return count

def part1():
    count = find_words_horizontal(prompt)
    count += find_words_vertical(prompt)
    count += find_words_diagonal(prompt)

    flipped = prompt.copy()
    for i in range(len(flipped)):
        flipped[i] = list(flipped[i])
        flipped[i].reverse()
        flipped[i] = ''.join(flipped[i])
    count += find_words_diagonal(flipped)

    print(count)

def find_x_mas(lines):
    diag1 = lines[0][0] + lines[1][1] + lines[2][2]
    diag2 = lines[0][2] + lines[1][1] + lines[2][0]
    if (diag1 == 'MAS' or diag1=='SAM') and (diag2 == 'MAS' or diag2=='SAM'):
        return 1
    return 0

def part2():
    count = 0
    for i in range(len(prompt)-2):
        for j in range(len(prompt[0])-2):
            lines = [prompt[i][j:j+3], prompt[i+1][j:j+3], prompt[i+2][j:j+3]]
            count += find_x_mas(lines)
    print(count)
    
part2()