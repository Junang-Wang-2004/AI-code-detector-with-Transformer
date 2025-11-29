class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        v1 = sum(a1) - a2
        v2 = -1
        v3 = v4 = 0
        for v5 in range(len(a1)):
            v3 += a1[v5]
            while v4 < len(a1) and v3 > v1:
                v3 -= a1[v4]
                v4 += 1
            if v3 == v1:
                v2 = max(v2, v5 - v4 + 1)
        return len(a1) - v2 if v2 != -1 else -1
