import numpy as np

with open('day6.txt') as f:
    fish = np.array([int(i) for i in f.read().split(',')])

fishcounts = np.bincount(fish).astype(np.int64)
fishcounts.resize(9, refcheck=False)

for i in range(0, 256):
    fishcounts = np.roll(fishcounts,-1)
    fishcounts[6] += fishcounts[8]

print(sum(fishcounts))