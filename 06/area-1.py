# part 1

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

gridSize = 0
beacons = {}

f = open('input.txt', 'r')
for i, line in enumerate(f):
    x, y = [int(coord.strip()) for coord in line.split(',')]
    gridSize = max(gridSize, x, y)
    beacons[(x,y)] = str(i)

gridSize += 1
grid = [['.' for i in xrange(gridSize)] for i in xrange(gridSize)]
for coords, label in beacons.items():
    x, y = coords
    grid[x][y] = label

def printGrid(beacons, grid):
    for x in range(gridSize):
        for y in range(gridSize):
            pixel = grid[y][x] # how come AoC x,y is Euclidean x,-y :sadface:
            if (y,x) in beacons:
                print colors.OKBLUE + pixel + colors.ENDC,
            else:
                print pixel,
            if y == gridSize - 1:
                print ""

def mhd(p1, p2, q1, q2):
    return abs(p1 - q1) + abs(p2 - q2)

def markClosestBeacon(p1, p2, beacons, grid):
    tie = None
    closest = None
    closestBeacon = None
    for coords, label in beacons.items():
        q1, q2 = coords
        if p1 == q1 and p2 == q2:
            return
        distance = mhd(p1, p2, q1, q2)
        if closest:
            if distance == closest:
                tie = distance
        if closest is None or distance < closest:
            closest = distance
            closestBeacon = label

    if tie and tie == closest:
        grid[p1][p2] = '.'
    else:
        grid[p1][p2] = closestBeacon

def findInfinites(grid):
    infinites = set()
    for i in range(gridSize):
        if grid[0][i] != '.':
            infinites.add(grid[0][i])
        if grid[i][0] != '.':
            infinites.add(grid[i][0])
        if grid[i][-1] != '.':
            infinites.add(grid[i][-1])
        if grid[-1][i] != '.':
            infinites.add(grid[-1][i])
    return infinites

def countMatches(label, grid):
    count = 0
    for x in range(gridSize):
        for y in range(gridSize):
            if grid[x][y] == label:
                count += 1
    return count

for x in range(gridSize):
    for y in range(gridSize):
        markClosestBeacon(x, y, beacons, grid)

infinites = findInfinites(grid)
largest = 0
for label in beacons.values():
    if label not in infinites:
        largest = max(largest, countMatches(label, grid))

print largest
