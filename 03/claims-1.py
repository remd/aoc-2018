# part 1

fabric = dict()
claims = []
answer = 0

f = open('input.txt', 'r')
for claim in f:
    x, y = [int(tmp) for tmp in claim.split(' ')[2].rstrip(':').split(',')]
    width, height = [int(tmp) for tmp in claim.split(' ')[3].split('x')]
    claims.append([x, y, width, height])
    for i in range(x, x + width):
        for j in range(y, y + height):
            try:
                if fabric[(i, j)] == 1:
                    fabric[(i, j)] = 2
                    answer += 1
            except KeyError:
                fabric[(i, j)] = 1
print answer
