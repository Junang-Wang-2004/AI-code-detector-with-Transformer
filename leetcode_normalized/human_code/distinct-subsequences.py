class C1(object):

    def numDistinct(self, a1, a2):
        v1 = [0 for v2 in range(len(a2) + 1)]
        v1[0] = 1
        for v3 in a1:
            for v4, v5 in reversed(list(enumerate(a2))):
                if v3 == v5:
                    v1[v4 + 1] += v1[v4]
        return v1[len(a2)]
