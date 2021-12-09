import itertools

with open('day8.txt') as f:
    entries = [i.split(' | ') for i in f.read().splitlines()]

ans = 0
for left,right in entries:
    for i in right.split():
        if len(i) in [2,3,4,7]:
            ans+=1
print(ans)

ans = 0
for left,right in entries:
    leftLengths = dict([(len(i),set(i)) for i in left.split()])
    result = ''
    for output in [set(i) for i in right.split()]:
        a = len(output)
        b = len(output.intersection(leftLengths[4]))
        c = len(output.intersection(leftLengths[2]))
        if(a==2):
            result += '1'; continue
        if(a==3):
            result += '7'; continue
        if(a==4):
            result += '4'; continue
        if(a==7):
            result += '8'; continue
        if(a==5 and b==2):
            result += '2'; continue
        if(a==5 and b==3 and c==1):
            result += '5'; continue
        if(a==5 and b==3 and c==2):
            result += '3'; continue
        if(a==6 and b==4):
            result += '9'; continue
        if(a==6 and b==3 and c==1):
            result += '6'; continue
        else:
            result += '0'
    ans += int(result)

print(ans)