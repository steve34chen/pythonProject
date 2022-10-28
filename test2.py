INPUT_FILE = "02_input.txt"

with open(INPUT_FILE, 'r') as f:
    data = [x for x in f.read().split("\n")]

x = 0
y = 0
for xx in data:
    xx = xx.split()
    if xx[0] == "forward":
        x += int(xx[1])
    elif xx[0] == "down":
        y += int(xx[1])
    else:
        y -= int(xx[1])

print("part1 ", x, y , x*y)


aim = 0
x = 0
y = 0
for xx in data:
    xx = xx.split()
    if xx[0] == "forward":
        y += (aim * int(xx[1]))
        x += int(xx[1])
    elif xx[0] == "down":
        aim += int(xx[1])
    else:
        aim -= int(xx[1])

print("part2 ", x, y , x*y)
