# part 2

fabric = dict()
claims = []

f = open('input.txt', 'r')
for claimId, claim in enumerate(f):
    x, y = [int(tmp) for tmp in claim.split(' ')[2].rstrip(':').split(',')]
    width, height = [int(tmp) for tmp in claim.split(' ')[3].split('x')]
    claims.append([claimId + 1, x, y, width, height])
    for i in range(x, x + width):
        for j in range(y, y + height):
            try:
                if fabric[(i, j)] == 1:
                    fabric[(i, j)] = 2
            except KeyError:
                fabric[(i, j)] = 1

for claimId, x, y, width, height in claims:
    overlaps = False
    for i in range(x, x + width):
        for j in range(y, y + height):
            if fabric[(i, j)] == 2:
                overlaps = True
    if not overlaps:
        print claimId
        break
