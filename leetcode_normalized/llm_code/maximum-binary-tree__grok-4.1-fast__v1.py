class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def constructMaximumBinaryTree(self, a1):
        v1 = []
        for v2 in range(len(a1) - 1, -1, -1):
            v3 = C1(a1[v2])
            while v1 and a1[v2] > v1[-1].val:
                v3.right = v1.pop()
            if v1:
                v1[-1].left = v3
            v1.append(v3)
        return v1[0]
