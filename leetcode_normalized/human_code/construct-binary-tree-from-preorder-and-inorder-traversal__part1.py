class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def buildTree(self, a1, a2):
        v1 = {}
        for v2, v3 in enumerate(a2):
            v1[v3] = v2
        return self.buildTreeRecu(v1, a1, a2, 0, 0, len(a2))

    def buildTreeRecu(self, a1, a2, a3, a4, a5, a6):
        if a5 == a6:
            return None
        v1 = C1(a2[a4])
        v2 = a1[a2[a4]]
        v1.left = self.buildTreeRecu(a1, a2, a3, a4 + 1, a5, v2)
        v1.right = self.buildTreeRecu(a1, a2, a3, a4 + 1 + v2 - a5, v2 + 1, a6)
        return v1
