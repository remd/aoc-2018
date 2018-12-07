# part 2
from operator import attrgetter
from re import findall
from string import uppercase as ALPHABHET

workerCount = 5
effort = 60

class Worker():
    def __init__(self):
        self.task = ""
        self.timeLeft = 0
        self.busy = False
        self.done = False
        
    
    def give(self, task):
        self.task = task
        self.timeLeft = ALPHABHET.index(task) + 1 + effort
        self.busy = True
        self.done = False

    def work(self):
        self.timeLeft -= 1
        if not self.timeLeft:
            self.done = True
    
    def finish(self):
        ret = self.task
        self.task = ""
        self.busy = False
        self.done = False
        self.timeLeft = 0
        return ret
    
    def __str__(self):
        if self.busy:
            return "task: %s, timeLeft: %d" % (self.task, self.timeLeft)
        else:
            return ""

class Step():
    def __init__(self, label, ancestors=[]):
        self.completed = False
        self.label = label
        self.ancestors = ancestors

    def __str__(self):
        return "{'%s':%s}" % (self.label, self.ancestors)

def available(steps, workers):
    alreadyAssigned = [worker.task for worker in workers if worker.busy]
    available = []
    for step in steps.values():
        if step.label not in alreadyAssigned and not step.completed and len(step.ancestors) == 0:
            available.append(step.label)
    return sorted(available)

def assign(tasks, workers):
    for worker in workers:
        if not worker.busy and tasks:
            worker.give(tasks.pop())

steps = {}
workers = [Worker() for i in range(workerCount)]

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

tick = 0
tasks = available(steps, workers)
assign(tasks, workers)
while len([step for step in steps.values() if not step.completed]):
    for worker in sorted(workers):
        if worker.done:
            finished = worker.finish()
            try:
                del steps[finished]
            except KeyError:
                print finished
                print steps
            for step in steps.values():
                if finished in step.ancestors:
                    step.ancestors.remove(finished)
    tasks = available(steps, workers)
    assign(tasks, workers)
    tick += 1
    [worker.work() for worker in workers]

print tick - 1
