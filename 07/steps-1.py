from re import findall

class Step():
    def __init__(self, label, ancestors=[]):
        self.completed = False
        self.label = label
        self.ancestors = ancestors

    def __str__(self):
        return "{'%s':%s}" % (self.label, self.ancestors)

def available(steps):
    available = []
    for step in steps.values():
        if not step.completed and len(step.ancestors) == 0:
            available.append(step.label)
    return sorted(available)

steps = {}
order = ""

f = open('input.txt', 'r')

allLabels = set()
for line in f:
    ancestor, label = [s.strip() for s in findall(" [A-Z] ", line)]
    allLabels.update(ancestor, label)
    try:
        steps[label].ancestors.append(ancestor)
    except KeyError:
        steps[label] = Step(label, [ancestor])

# add labels with no ancestors
for label in allLabels:
    if label not in steps:
        steps[label] = Step(label)

remaining = available(steps)
while len(remaining):
    currentStep = remaining[0]
    steps[currentStep].completed = True
    for step in steps.values():
        if currentStep in step.ancestors:
            step.ancestors.remove(currentStep)
    order += currentStep
    remaining = available(steps)

print order
