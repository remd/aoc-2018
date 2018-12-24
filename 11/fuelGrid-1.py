# part 1

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

def calculateTotal(powerGrid, x, y):
    return safeGet(powerGrid, x, y) + \
           safeGet(powerGrid, x+1, y) + \
           safeGet(powerGrid, x+2, y) + \
           safeGet(powerGrid, x, y+1) + \
           safeGet(powerGrid, x, y+2) + \
           safeGet(powerGrid, x+1, y+1) + \
           safeGet(powerGrid, x+1, y+2) + \
           safeGet(powerGrid, x+2, y+1) + \
           safeGet(powerGrid, x+2, y+2) 


assert calculatePower(3, 5, 8) == 4
assert calculatePower(122, 79, 57) == -5
assert calculatePower(217, 196, 39) == 0
assert calculatePower(101, 153, 71) == 4

powerGrid = [[0 for i in xrange(300)] for i in xrange(300)]

for x in range(300):
    for y in range(300):
        powerGrid[x][y] = calculatePower(x, y)

largest = 0
ansX = 0
ansY = 0
for x in range(300):
    for y in range(300):
        total = calculateTotal(powerGrid, x, y)
        if total > largest:
            largest = total
            ansX = x
            ansY = y

print "(%d, %d): %d" % (ansX, ansY, largest)
