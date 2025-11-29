class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def constructFromPrePost(self, a1, a2):
        v1 = {a2[i]: i for v2 in range(len(a2))}

        def build(a1, a2, a3):
            if a3 == 0:
                return None
            v1 = C1(a1[a1])
            if a3 > 1:
                v2 = v1[a1[a1 + 1]] - a2 + 1
                v1.left = build(a1 + 1, a2, v2)
                v1.right = build(a1 + 1 + v2, a2 + v2, a3 - v2 - 1)
            return v1
        return build(0, 0, len(a1))
