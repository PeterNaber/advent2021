import numpy as np;

with open('day3.txt') as f:
    matrix = np.array([list(i) for i in f.read().splitlines()]).astype(int)

def toInt(bits):
    return int("".join([str(x) for x in bits]),2)

#part 1
gam = []
for i in matrix.transpose():
    mc = 1 if (i == 1).sum() >= (i == 0).sum() else 0
    gam.append(mc)
eps = [1-i for i in gam]

print(toInt(gam)*toInt(eps))

#part 2
o = matrix
i = 0
while len(o) > 1:
    mc = 1 if (o[:,i] == 1).sum() >= (o[:,i] == 0).sum() else 0
    o = o[o[:,i] == mc]
    i += 1

s = matrix
i = 0
while len(s) > 1:
    mc = 1 if (s[:,i] == 1).sum() >= (s[:,i] == 0).sum() else 0
    s = s[s[:,i] != mc]
    i += 1

print(toInt(o[0])*toInt(s[0]))
