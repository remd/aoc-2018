# part 1
f = open('input.txt', 'r')
guards = dict()
asleepAt = dict()

badge = None
sleepStart = None
sleepEnd = None
for line in f:
    if '#' in line:
        badge = int(line.split()[3][1:])
        if badge not in guards.keys():
            guards[badge] = 0
            asleepAt[badge] = dict()
            for minute in range(0, 60):
                asleepAt[badge][minute] = 0
    elif 'sleep' in line:
        sleepStart = int(line.split()[1][3:5])
    else:
        sleepEnd = int(line.split()[1][3:5])
        for minute in range(sleepStart, sleepEnd):
            guards[badge] += 1
            asleepAt[badge][minute] += 1

insomniacBadge = max(guards, key=guards.get)
sleepiestMinute = max(asleepAt[insomniacBadge], key=asleepAt[insomniacBadge].get)

print sleepiestMinute * insomniacBadge

# part 2

mostFrequentMinute = 0
frequency = 0
frequentBadge = None
for k in guards.keys():
    for x in range(0, 60):
        if asleepAt[k][x] > frequency:
            mostFrequentMinute = x
            frequency = asleepAt[k][x]
            frequentBadge = k

print frequentBadge * mostFrequentMinute
