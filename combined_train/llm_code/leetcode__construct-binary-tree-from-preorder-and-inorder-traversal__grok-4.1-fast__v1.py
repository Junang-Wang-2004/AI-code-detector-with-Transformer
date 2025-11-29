class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def buildTree(self, a1, a2):
        v1 = {val: idx for v2, v3 in enumerate(a2)}
        v4 = [0]

        def construct(a1, a2):
            if a1 > a2:
                return None
            v1 = a1[v4[0]]
            v4[0] += 1
            v2 = C1(v1)
            v3 = v1[v1]
            v2.left = construct(a1, v3 - 1)
            v2.right = construct(v3 + 1, a2)
            return v2
        return construct(0, len(a2) - 1)
