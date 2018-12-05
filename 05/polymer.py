import string

def clean(polymer, unit):
    return polymer.replace(unit, "").replace(unit.upper(), "")

def reaction(polymer):
    for c in range(len(polymer)-1):
        if polymer[c] != polymer[c+1] and polymer[c].lower() == polymer[c+1].lower():
            try:
                return polymer[:c] + polymer[c+2:]
            except IndexError:
                return polymer[:c]
    return polymer # unchanged

def fullyReact(polymer):
    before = len(polymer)
    polymer = reaction(polymer)
    after = len(polymer)
    while before != after:
        before = after
        polymer = reaction(polymer)
        after = len(polymer)
    return polymer

f = open('input.txt', 'r')
polymer = f.readlines()[0].strip()

# part 1

print len(fullyReact(polymer))

# part 2

shortest = None
for unit in string.ascii_lowercase:
    trial = len(fullyReact(clean(polymer, unit)))
    if shortest is None or trial < shortest:
        shortest = trial

print shortest
