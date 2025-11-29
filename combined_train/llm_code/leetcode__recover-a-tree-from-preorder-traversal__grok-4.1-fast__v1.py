class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def recoverFromPreorder(self, a1):

        def construct(a1, a2):
            if a2 >= len(a1):
                return (None, a2)
            v1 = a2
            v2 = 0
            while v1 < len(a1) and a1[v1] == '-':
                v2 += 1
                v1 += 1
            if v2 != a1:
                return (None, a2)
            v3 = v1
            while v1 < len(a1) and a1[v1] != '-':
                v1 += 1
            v4 = C1(int(a1[v3:v1]))
            v5, a2 = construct(a1 + 1, v1)
            v4.left = v5
            v7, a2 = construct(a1 + 1, a2)
            v4.right = v7
            return (v4, a2)
        v1, v2 = construct(0, 0)
        return v1
