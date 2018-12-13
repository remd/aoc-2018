# part 1 is first output
# part 2 is second output

from re import findall
from operator import attrgetter

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Player():
    def __init__(self):
        self.score = 0

def printGame(circle, currentPlayer, currentMarble):
    print "[%2d] " % currentPlayer,
    for i in range(len(circle)):
        if currentMarble == i:
            print "%s%d%s" % (colors.OKGREEN, circle[i], colors.ENDC),
        else:
            print circle[i],
    print


for line in open('input.txt', 'r'):
    playerCount, marbleCount = [int(s.strip()) for s in findall("[0-9]+", line)]

    print "==== NEW GAME ===="
    print "= P: %02d  M: %04d =" % (playerCount, marbleCount)
    print "=================="
    players = [Player() for i in range(playerCount)]
    circle = [0]
    currentPlayer = 0
    currentMarble = 0
    for i in range(1, marbleCount+1):
        if i % 23 == 0:
            player = players[currentPlayer]
            player.score += i
            currentMarble = (currentMarble - 7) % len(circle)
            player.score += circle.pop(currentMarble)
        else:
            target = (currentMarble + 2) % len(circle)
            if target == 0:
                target = len(circle)
            circle.insert(target, i)
            currentMarble = circle.index(i)
        currentPlayer = (currentPlayer + 1) % playerCount

    print max(players, key=attrgetter('score')).score

