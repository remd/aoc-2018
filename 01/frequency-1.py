# part 1

f = open('input.txt', 'r')
frequency = 0

for line in f:
    frequency += int(line)

print frequency
