input = open('./input.txt', 'r')
lines = input.readlines()

def getPriority(item):
    if (item >= 'a'):
        return ord(item)-ord('a')+1
    return ord(item)-ord('A')+27

def part1(input):
    prioritySum = 0
    for line in input:
        half = int((len(line)-1)/2)
        for char in line[:half]:
            if line[half:].count(char) > 0:
                prioritySum += getPriority(char)
                break
    return prioritySum

def part2(input):
    prioritySum = 0
    for i in range(len(input)):
        if i % 3 == 0:
            elf1, elf2, elf3 = input[i], input[i+1], input[i+2]
            for char in elf1:
                if elf2.count(char) > 0 and elf3.count(char) > 0:
                    prioritySum += getPriority(char)
                    break
    return prioritySum

print('Part 1:', part1(lines))
print('Part 2:', part2(lines))
