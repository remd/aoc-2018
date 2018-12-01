# part 2

lines = open('input.txt', 'r').readlines()
frequency = 0
seen = set([0])
found = False

while found is False:
    for line in lines:
        frequency += int(line)
        if frequency in seen:
            print frequency
            found = True
            break
        else:
            seen.add(frequency)
