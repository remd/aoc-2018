# part 1

f = open('input.txt', 'r')
twoLetters = 0
threeLetters = 0

for boxId in f:
    checkSet = set()
    for letter in boxId:
        checkSet.add(letter)

    matchedTwo = False
    matchedThree = False
    for letter in checkSet:
        count = boxId.count(letter)
        if count is 2:
            matchedTwo = True
        elif count is 3:
            matchedThree = True
    
    if matchedTwo: twoLetters += 1
    if matchedThree: threeLetters += 1

print twoLetters * threeLetters
