with open('day2.txt') as f:
    cmds = [i.split(" ") for i in f.read().splitlines()] 

#part1
pos = dept = 0
for dir, val in cmds:
    pos += int(val) * int(dir == "forward")
    dept += int(val) * int((dir == "down") - (dir == "up"))
print(pos*dept)

#part2
pos = dept = aim = 0
for dir,val in cmds:
    aim += int(val) * int((dir == "down") - (dir == "up"))
    pos += int(val) * int(dir == "forward")
    dept += int(val) * int(dir == "forward") * aim
print(pos*dept)