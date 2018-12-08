# part 1
from string import uppercase as ALPHABHET

seek = 0
nodeCount = 0

class Node():
    def __init__(self, children=[], metadata=[], parent=None):
        self.children = children
        self.metadata = metadata
        self.parent = parent
    
    def __str__(self):
        return "Children: %s, Metadata: %s" % ([str(c) for c in self.children], self.metadata)

def read(data, parent=None):
    global seek
    global nodeCount
    root = Node([], [], parent)
    nodeCount += 1

    childrenCount = int(data[seek])
    seek += 1
    metadataCount = int(data[seek])
    seek += 1
    if childrenCount:
        for i in range(childrenCount):
            root.children.append(read(data, root))
    if metadataCount:
        for i in range(metadataCount):
            root.metadata.append(int(data[seek]))
            seek += 1
    return root

def sumMetadata(root):
    total = 0
    if root.metadata:
        for n in root.metadata:
            total += n
    for child in root.children:
        total += sumMetadata(child)
    return total


data = open('input.txt', 'r').readlines()[0].split(' ')

root = read(data)
print sumMetadata(root)
