class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def intersect(self, n1, n2):
        if n1.isLeaf and n2.isLeaf:
            return Node(n1.val or n2.val, True, None, None, None, None)
        ch1 = (n1,) * 4 if n1.isLeaf else (n1.topLeft, n1.topRight, n1.bottomLeft, n1.bottomRight)
        ch2 = (n2,) * 4 if n2.isLeaf else (n2.topLeft, n2.topRight, n2.bottomLeft, n2.bottomRight)
        tL = self.intersect(ch1[0], ch2[0])
        tR = self.intersect(ch1[1], ch2[1])
        bL = self.intersect(ch1[2], ch2[2])
        bR = self.intersect(ch1[3], ch2[3])
        children = [tL, tR, bL, bR]
        if all(c.isLeaf for c in children) and len(set(c.val for c in children)) <= 1:
            return Node(children[0].val, True, None, None, None, None)
        return Node(True, False, tL, tR, bL, bR)
