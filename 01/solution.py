input = open('./input.txt', 'r')
lines = input.readlines()

currentElfTotal = 0
elfTotals = []
for line in lines:
    if line.strip():
        currentElfTotal += int(line)
    else:
        elfTotals.append(currentElfTotal)
        currentElfTotal = 0

elfTotals.sort(reverse=True)
print('Part 1:', elfTotals[0])
print('Part 2:', sum(elfTotals[:3]))