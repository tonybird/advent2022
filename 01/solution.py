file1 = open('./input.txt', 'r')
lines = file1.readlines()

currentElfTotal = 0
elfTotals = []
for line in lines:
    if line.strip():
        currentElfTotal += int(line)
    else:
        elfTotals.append(currentElfTotal)
        currentElfTotal = 0
        continue

elfTotals.sort(reverse=True)
print(sum(elfTotals[:3]))
