# part 2

def safeGet(matrix, x, y):
    try:
        return matrix[x][y]
    except IndexError:
        return 0

def calculatePower(x, y, sn=9435):
    rack = x + 10
    power = rack * y
    power += sn
    power = power * rack
    power = (power / 100) % 10
    power -= 5
    return power

def calculateSum(powerGrid, sat, x, y):
    return safeGet(powerGrid, x, y) + \
           safeGet(sat, x, y-1) + \
           safeGet(sat, x-1, y) - \
           safeGet(sat, x-1, y-1) 

def sumArea(sat, x, y, size):
    return safeGet(sat, x+size, y+size) + \
           safeGet(sat, x, y) - \
           safeGet(sat, x+size, y) - \
           safeGet(sat, x, y+size)

assert calculatePower(3, 5, 8) == 4
assert calculatePower(122, 79, 57) == -5
assert calculatePower(217, 196, 39) == 0
assert calculatePower(101, 153, 71) == 4

powerGrid = [[0 for i in xrange(300)] for i in xrange(300)]
summedAreaTable = [[0 for i in xrange(300)] for i in xrange(300)]

for x in range(300):
    for y in range(300):
        powerGrid[x][y] = calculatePower(x, y)

for x in range(300):
    for y in range(300):
        summedAreaTable[x][y] = calculateSum(powerGrid, summedAreaTable, x, y)

largest = 0
ansX = 0
ansY = 0
size = 0
for x in range(300):
    for y in range(300):
        maxSize = 300 - max(x, y)
        # print "Top-left (%d, %d), max size is %d" % (x, y, maxSize)
        if maxSize >= 0:
            for z in range(1, maxSize):
                total = sumArea(summedAreaTable, x, y, z)
                if total > largest:
                    largest = total
                    size = z
                    ansX = x
                    ansY = y

# compensate for zero-based indices
print "(%d, %d, %d): %d" % (ansX + 1, ansY + 1, size, largest)
