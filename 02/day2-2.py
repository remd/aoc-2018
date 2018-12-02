# part 2

def difference(seq1, seq2):
    return sum(1 for a, b in zip(seq1, seq2) if a != b)

f = open('input.txt', 'r')

boxes = []

for boxId in f:
    boxes.append(boxId)

for boxIdA in boxes:
    for boxIdB in boxes:
        if difference(boxIdA, boxIdB) is 1:
            print boxIdA, boxIdB
            exit()
