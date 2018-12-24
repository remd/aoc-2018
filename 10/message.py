from re import findall
from time import sleep

class Point:
    def __init__(self, x, y, xvel, yvel):
        self.x = int(x)
        self.y = int(y)
        self.xvel = int(xvel)
        self.yvel = int(yvel)
    
    def tick(self):
        self.x += self.xvel
        self.y += self.yvel
    
    def __str__(self):
        return "(%d, %d) moving (%d, %d) per tick" % (self.x, self.y, self.xvel, self.yvel)

def tick(points):
    for point in points:
        point.tick()

def findPoint(points, x, y):
    for point in points:
        if point.x == x and point.y == y:
            return True
    return False

def printGrid(points, xmin, xmax, ymin, ymax):
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if findPoint(points, x, y):
                print '#',
            else:
                print '.',
        print

points = []
f = open("input.txt", 'r')

for line in f:
    position, velocity = [[result.strip() for result in s.split(',')] for s in findall("\s*\-?[0-9]+,\s*\-?[0-9]+", line)]
    points.append(Point(position[0], position[1], velocity[0], velocity[1]))

ticks = 0
while True:
    xmin = min(point.x for point in points)
    ymin = min(point.y for point in points)
    xmax = max(point.x for point in points)
    ymax = max(point.y for point in points)
    if (xmax - xmin) <= 100 and (ymax - ymin) <= 100:
        printGrid(points, xmin, xmax, ymin, ymax)
        print(ticks)
        sleep(1)
        print
    tick(points)
    ticks += 1
