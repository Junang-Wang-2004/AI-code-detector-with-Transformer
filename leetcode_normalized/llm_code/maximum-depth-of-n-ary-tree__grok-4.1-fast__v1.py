class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def maxDepth(self, a1):
        v1 = 0
        v2 = []
        if a1:
            v2.append((a1, 1))
        while v2:
            v3, v4 = v2.pop()
            if v4 > v1:
                v1 = v4
            for v5 in v3.children:
                v2.append((v5, v4 + 1))
        return v1
