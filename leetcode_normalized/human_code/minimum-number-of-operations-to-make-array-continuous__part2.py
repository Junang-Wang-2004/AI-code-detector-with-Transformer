class C1(object):

    def minOperations(self, a1):
        """
        """
        v1 = len(a1)
        a1 = sorted(set(a1))
        v3 = v4 = 0
        for v5 in range(len(a1)):
            while v4 < len(a1) and a1[v4] <= a1[v5] + v1 - 1:
                v4 += 1
            v3 = max(v3, v4 - v5)
        return v1 - v3
