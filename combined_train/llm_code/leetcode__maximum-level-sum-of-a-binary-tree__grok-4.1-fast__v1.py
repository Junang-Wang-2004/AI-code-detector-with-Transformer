class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxLevelSum(self, a1):
        v1 = []
        v2 = [a1]
        while v2:
            v3 = []
            v4 = 0
            for v5 in v2:
                v4 += v5.val
                if v5.left:
                    v3.append(v5.left)
                if v5.right:
                    v3.append(v5.right)
            v1.append(v4)
            v2 = v3
        v6 = max(v1)
        return v1.index(v6) + 1
