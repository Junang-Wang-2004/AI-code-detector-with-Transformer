class C1(object):

    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.val = a1
        self.isLeaf = a2
        self.topLeft = a3
        self.topRight = a4
        self.bottomLeft = a5
        self.bottomRight = a6

class C2(object):

    def construct(self, a1):

        def build(a1, a2, a3):
            v1 = a1[a1][a2] == 1
            v2 = True
            for v3 in range(a3):
                v4 = a1 + v3
                for v5 in range(a3):
                    v6 = a2 + v5
                    if (a1[v4][v6] == 1) != v1:
                        v2 = False
                        break
                if not v2:
                    break
            if v2:
                return C1(v1, True, None, None, None, None)
            v7 = a3 // 2
            return C1(True, False, build(a1, a2, v7), build(a1, a2 + v7, v7), build(a1 + v7, a2, v7), build(a1 + v7, a2 + v7, v7))
        v1 = len(a1)
        return None if v1 == 0 else build(0, 0, v1)
