class C1(object):

    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.val = a1
        self.isLeaf = a2
        self.topLeft = a3
        self.topRight = a4
        self.bottomLeft = a5
        self.bottomRight = a6

class C2(object):

    def intersect(self, a1, a2):
        if a1.isLeaf and a2.isLeaf:
            return C1(a1.val or a2.val, True, None, None, None, None)
        v1 = (a1,) * 4 if a1.isLeaf else (a1.topLeft, a1.topRight, a1.bottomLeft, a1.bottomRight)
        v2 = (a2,) * 4 if a2.isLeaf else (a2.topLeft, a2.topRight, a2.bottomLeft, a2.bottomRight)
        v3 = self.intersect(v1[0], v2[0])
        v4 = self.intersect(v1[1], v2[1])
        v5 = self.intersect(v1[2], v2[2])
        v6 = self.intersect(v1[3], v2[3])
        v7 = [v3, v4, v5, v6]
        if all((c.isLeaf for v8 in v7)) and len(set((v8.val for v8 in v7))) <= 1:
            return C1(v7[0].val, True, None, None, None, None)
        return C1(True, False, v3, v4, v5, v6)
