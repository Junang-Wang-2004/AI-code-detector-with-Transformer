class C1(object):

    def maximumSubsequenceCount(self, a1, a2):
        v1, v2 = a2
        v3 = 0
        v4 = 0
        v5 = 0
        v6 = 0
        v7 = len(a1)
        v8 = v7 - 1
        while v8 >= 0:
            v9 = a1[v8]
            if v9 == v1:
                v3 += v4
                v5 += 1
            if v9 == v2:
                v4 += 1
                v6 += 1
            v8 -= 1
        return v3 + max(v5, v6)
