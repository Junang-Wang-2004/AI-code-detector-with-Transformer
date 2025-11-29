class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def buildTree(self, a1, a2):
        if not a1:
            return None
        v1 = {val: idx for v2, v3 in enumerate(a1)}

        def construct(a1, a2, a3, a4):
            if a1 > a2 or a3 > a4:
                return None
            v1 = a2[a4]
            v2 = C1(v1)
            v3 = v1[v1]
            v4 = v3 - a1
            v2.left = construct(a1, v3 - 1, a3, a3 + v4 - 1)
            v2.right = construct(v3 + 1, a2, a3 + v4, a4 - 1)
            return v2
        return construct(0, len(a1) - 1, 0, len(a2) - 1)
