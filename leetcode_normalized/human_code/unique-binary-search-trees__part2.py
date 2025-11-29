class C1(object):

    def numTrees(self, a1):
        v1 = [1, 1]
        for v2 in range(2, a1 + 1):
            v3 = 0
            for v4 in range(v2):
                v3 += v1[v4] * v1[v2 - v4 - 1]
            v1.append(v3)
        return v1[-1]
