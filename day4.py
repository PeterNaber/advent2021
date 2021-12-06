import numpy as np

with open('day4a.txt') as f:
    numbers = [int(i) for i in f.read().split(',')]
with open('day4b.txt') as f:
    boards = [i.split() for i in f.read().splitlines()]
boards = np.array([boards[i : i + 5] for i in range(0, len(boards), 6)]).astype(int)
hits = np.zeros(boards.shape)

def isWinner(hit):
    return 5 in hit.sum(0) or 5 in hit.sum(1)

#part 1
for number in numbers:
    called = number
    hits += boards == number
    winners = np.array([isWinner(x) for x in hits])
    if (any(winners)):
        break

sum = np.sum(boards[winners]*(1-hits[winners]))
print(sum*called)

#part 2
hits = np.zeros(boards.shape)

for number in numbers:
    called = number
    hits += boards == number
    remainers = [isWinner(x) == False for x in hits]
    if not any(remainers):
        break
    boards = boards[remainers]
    hits = hits[remainers]
        
sum = np.sum(boards[0]*(1-hits[0]))
print(sum*called)