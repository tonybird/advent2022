input= open('./input.txt', 'r')
lines= input.readlines()

winPoints, drawPoints, lossPoints = 6, 3, 0
pointsForShape = {'rock': 1, 'paper': 2, 'scissors': 3}
shape = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

def part1(input):
    pointsForOutcome = {
        'rock': {'rock': drawPoints, 'paper': winPoints, 'scissors': lossPoints},
        'paper': {'rock': lossPoints, 'paper': drawPoints, 'scissors': winPoints},
        'scissors': {'rock': winPoints, 'paper': lossPoints, 'scissors': drawPoints}}
    score = 0
    for line in input:
        opponent, self = line.strip().split(' ')
        score += pointsForShape[shape[self]] + pointsForOutcome[shape[opponent]][shape[self]]
    return score
print('Part 1:', part1(lines))

def part2(input):
    winAgainst= {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    loseAgainst= {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
    score= 0
    for line in input:
        opponent, outcome = line.strip().split(' ')
        if outcome == 'X':
            score += lossPoints + pointsForShape[loseAgainst[shape[opponent]]]
        elif outcome == 'Y':
            score += drawPoints + pointsForShape[shape[opponent]]
        elif outcome == 'Z':
            score += winPoints + pointsForShape[winAgainst[shape[opponent]]]
    return score
print('Part 2:', part2(lines))
