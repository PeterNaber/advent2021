from numpy.lib.function_base import median

with open('day7.txt') as f:
    crabs = [int(i) for i in f.read().split(',')]

print(sum(abs(crabs - median(crabs))))

def f(d): return d*(d+1)/2
print(min(sum(f(abs(x - y)) for y in crabs) for x in crabs))