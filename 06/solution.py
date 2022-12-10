line = open('./input.txt', 'r').readline()

def findFirstUniqueWindow(windowSize):
    for i in range(len(line)-windowSize):
        window = line[i:i+windowSize]
        if len(window) == len(set(window)):
            return i+windowSize

print('Part 1:', findFirstUniqueWindow(4))
print('Part 2:', findFirstUniqueWindow(14))