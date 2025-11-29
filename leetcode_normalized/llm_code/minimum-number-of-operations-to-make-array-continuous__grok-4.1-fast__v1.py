class C1:

    def minOperations(self, a1):
        a1.sort()
        v1 = []
        for v2 in a1:
            if not v1 or v1[-1] != v2:
                v1.append(v2)
        v3 = len(a1)
        v4 = 0
        v5 = 0
        for v6 in range(len(v1)):
            while v1[v6] - v1[v5] > v3 - 1:
                v5 += 1
            v4 = max(v4, v6 - v5 + 1)
        return v3 - v4
