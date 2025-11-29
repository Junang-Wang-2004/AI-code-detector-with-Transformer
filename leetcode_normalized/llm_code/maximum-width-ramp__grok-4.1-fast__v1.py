class C1:

    def maxWidthRamp(self, a1):
        v1 = len(a1)
        v2 = []
        for v3 in range(v1):
            if not v2 or a1[v2[-1]] > a1[v3]:
                v2.append(v3)
        v4 = 0
        for v5 in range(v1 - 1, -1, -1):
            while v2 and a1[v2[-1]] <= a1[v5]:
                v4 = max(v4, v5 - v2.pop())
        return v4
