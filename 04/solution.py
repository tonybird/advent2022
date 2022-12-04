input = open('./input.txt', 'r')
lines = input.readlines()

def parse(line):
    elf1, elf2 = line.split(',')
    elf1Start, elf1Stop = elf1.split('-')
    elf2Start, elf2Stop = elf2.split('-')
    return int(elf1Start), int(elf1Stop), int(elf2Start), int(elf2Stop)

part1 = 0
part2 = 0
for line in lines:
    elf1Start, elf1Stop, elf2Start, elf2Stop = parse(line)
    if (elf1Start >= elf2Start and elf1Stop <= elf2Stop) or (elf2Start >= elf1Start and elf2Stop <= elf1Stop):
        part1 += 1
    if (elf1Stop >= elf2Start and elf1Start <= elf2Stop) or (elf2Stop >= elf1Start and elf2Start <= elf1Stop):
        part2 += 1

print('Part 1:', part1)
print('Part 2:', part2)
