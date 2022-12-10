import copy
lines = open('./input.txt', 'r').readlines()

def getInitialStacks(lines):
    stacks = {}
    for line in lines:
        for i in range(9):
            if i+1 not in stacks:
                stacks[i+1] = []
            if line[4*i+1] != ' ':
                stacks[i+1].append(line[4*i+1])
    return stacks

def parse(line):
    _, count, _, start, _, end = line.strip().split(' ')
    return int(count), int(start), int(end)

def getTopCrates(stacks):
    result = ''
    for stack in stacks:
        result += stacks[stack][0]
    return result

def solve():
    part1 = getInitialStacks(lines[:8])
    part2 = copy.deepcopy(part1)
    for line in lines[10:]:
        count, start, end = parse(line)
        for i in range(count):
            crate = part1[start].pop(0)
            crate = part2[start].pop(0)
            part1[end].insert(0, crate)
            part2[end].insert(i, crate)
    return part1, part2

part1, part2 = solve()
print('Part 1:', getTopCrates(part1))
print('Part 2:', getTopCrates(part2))
