with open('day10.txt') as f:
    lines = [i for i in f.read().splitlines()]

symbols = {
    '(':')',
    '{':'}',
    '[':']',
    '<':'>'
}
points ={ 
')': 3,
']': 57,
'}': 1197,
'>': 25137,
}
addPoints ={ 
')': 1,
']': 2,
'}': 3,
'>': 4,
}

def scoreLine(line):
    check = []
    for char in line:
        if char in symbols.keys():
            check.append(char)
        if char in symbols.values():
            if char != symbols[check.pop()]:
                return points[char]
    return 0

print(sum([scoreLine(i) for i in lines]))

def scoreLineWithAuto(line):
    check = []
    for char in line:
        if char in symbols.keys():
            check.append(char)
        if char in symbols.values():
            if char != symbols[check.pop()]:
                return 0
    autoComplete = [symbols[i] for i in check]
    autoComplete.reverse()
    score = 0
    for i in autoComplete:
        score *= 5
        score += addPoints[i]
    return score

scores = [scoreLineWithAuto(i) for i in lines]
scores = [i for i in scores if i > 0]
scores.sort()
mid = scores[len(scores)//2]
print(mid)