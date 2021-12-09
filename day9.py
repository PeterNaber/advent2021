import numpy as np
from collections import deque

with open('day9.txt') as f:
    heightMap = np.array([[int(char) for char in i] for i in f.read().splitlines()])
xmax = len(heightMap)
ymax = len(heightMap[0])

def getSurround(x,y):
    points = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    return [(x,y) for x,y in points if 0 <= x < xmax and 0 <= y < ymax]

lows = []
lowPoints = []
for x,row in enumerate(heightMap):
    for y,value in enumerate(row):
        if all(value < heightMap[x][y] for x,y in getSurround(x,y)): 
            lows.append(value+1)
            lowPoints.append((x,y))        
print(sum(lows))

def getBasinSize(x, y):
    size = 1
    visited.add((x,y))
    for x, y in getSurround(x, y):
        if (x, y) not in visited and heightMap[x][y] != 9:
            size += getBasinSize(x, y)        
    return size

visited = set()
basins = [getBasinSize(x,y) for x,y in lowPoints]
basins.sort()
print(basins[-3]*basins[-2]*basins[-1])