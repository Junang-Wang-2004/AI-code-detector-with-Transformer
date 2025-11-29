class C1(object):

    def subArrayRanges(self, a1):
        """
        """
        v1 = 0
        v2 = []
        for v3 in range(len(a1) + 1):
            v4 = a1[v3] if v3 < len(a1) else float('inf')
            while v2 and a1[v2[-1]] <= v4:
                v5 = v2.pop()
                v6 = v2[-1] if v2 else -1
                v1 += a1[v5] * (v5 - v6) * (v3 - v5)
            v2.append(v3)
        v2 = []
        for v3 in range(len(a1) + 1):
            v4 = a1[v3] if v3 < len(a1) else float('-inf')
            while v2 and a1[v2[-1]] >= v4:
                v5 = v2.pop()
                v6 = v2[-1] if v2 else -1
                v1 -= a1[v5] * (v5 - v6) * (v3 - v5)
            v2.append(v3)
        return v1
