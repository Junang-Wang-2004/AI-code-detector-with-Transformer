class C1:

    def maximumImportance(self, a1, a2):
        v1 = [0] * a1
        for v2, v3 in a2:
            v1[v2] += 1
            v1[v3] += 1
        v1.sort(reverse=True)
        v4 = 0
        for v5 in range(a1):
            v4 += v1[v5] * (a1 - v5)
        return v4
