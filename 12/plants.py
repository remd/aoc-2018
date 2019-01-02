import traceback
# part 1
def debug(gen, pots):
    print "%02d: %s" % (gen, ''.join([pots[k] for k in sorted(pots)]))

# make room for potential next-generation plants
def prep(pots):
    left = min(pots)
    right = max(pots)
    for i in range(left-2, left):
        pots[i] = '.'
    for i in range(right+1, right+3):
        pots[i] = '.'

def neighbors(pots, currentIndex):
    try:
        return ''.join([pots[i] for i in range(currentIndex-2, currentIndex+3)])
    except KeyError:
        print currentIndex-2
        print currentIndex+3
        traceback.print_exc()
        print sorted(pots)
        exit()

f = open("test.txt", 'r')
initialState = f.readline().split(':')[-1].strip()
f.readline() # skip blank line

rules = []
for rule in f.readlines():
    before, after = [s.strip() for s in rule.split(" => ")]
    if after == '#':
        rules.append(before)

pots = {}
for i, c in enumerate(initialState):
    pots[i] = c

for generation in range(21):
    end = max(pots)
    nextGeneration = {}
    prep(pots)
    debug(generation, pots)
    for k in range(min(pots), len(pots)):
        nextGeneration[k] = '.'
    for k in range(min(pots)+2, end):
        if neighbors(pots, k) in rules:
            nextGeneration[k] = '#'
        # todo: our bug has something to do with when no rules match but pots[k] had a plant in it
    pots = nextGeneration

total = 0
for k, v in pots.items():
    if v == '#':
        total += k

print total
