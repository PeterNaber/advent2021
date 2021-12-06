import numpy as np

with open('day5.txt') as f:
    lines = np.array([[y.split(',') for y in x.split("->")] for x in f.read().splitlines()]).astype(int)
matrix = np.zeros((1000, 1000))

for (start,end) in lines:
    dx, dy = np.sign(end-start)
    if dx == 0 or dy == 0:
        while (start != end+[dx,dy]).any():
            matrix[start[0],start[1]] += 1
            start[0] += dx
            start[1] += dy

print((matrix > 1).sum())

for (start,end) in lines:
    dx, dy = np.sign(end-start)
    while (start != end+[dx,dy]).any():
        matrix[start[0],start[1]] += 1
        start[0] += dx
        start[1] += dy
        

print((matrix > 1).sum())