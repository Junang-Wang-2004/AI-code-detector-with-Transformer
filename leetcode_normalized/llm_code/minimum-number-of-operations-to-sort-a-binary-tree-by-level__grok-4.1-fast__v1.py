class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def minimumOperations(self, a1):
        if not a1:
            return 0
        v1 = 0
        v2 = [a1]
        while v2:
            v3 = []
            v4 = []
            for v5 in v2:
                v3.append(v5.val)
                if v5.left:
                    v4.append(v5.left)
                if v5.right:
                    v4.append(v5.right)
            v6 = len(v3)
            v7 = [(v3[k], k) for v8 in range(v6)]
            v7.sort()
            v9 = [False] * v6
            v10 = 0
            for v11 in range(v6):
                if v9[v11]:
                    continue
                v10 += 1
                v12 = v11
                while not v9[v12]:
                    v9[v12] = True
                    v12 = v7[v12][1]
            v1 += v6 - v10
            v2 = v4
        return v1
