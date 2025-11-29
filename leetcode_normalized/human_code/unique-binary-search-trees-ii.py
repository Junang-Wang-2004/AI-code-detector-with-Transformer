class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            v1 = []
            v2 = [self]
            while v2:
                v3 = v2[0]
                if v3:
                    v1.append(v3.val)
                    v2.append(v3.left)
                    v2.append(v3.right)
                else:
                    v1.append('#')
                v2 = v2[1:]
            while v1[-1] == '#':
                v1.pop()
            return repr(v1)
        else:
            return None

class C2(object):

    def generateTrees(self, a1):
        return self.generateTreesRecu(1, a1)

    def generateTreesRecu(self, a1, a2):
        v1 = []
        if a1 > a2:
            v1.append(None)
        for v2 in range(a1, a2 + 1):
            v3 = self.generateTreesRecu(a1, v2 - 1)
            v4 = self.generateTreesRecu(v2 + 1, a2)
            for v5 in v3:
                for v6 in v4:
                    v7 = C1(v2)
                    v7.left = v5
                    v7.right = v6
                    v1.append(v7)
        return v1
