class C1:

    def maximumUniqueSubarray(self, a1):
        v1 = set()
        v2 = 0
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            while a1[v5] in v1:
                v2 -= a1[v4]
                v1.remove(a1[v4])
                v4 += 1
            v1.add(a1[v5])
            v2 += a1[v5]
            v3 = max(v3, v2)
        return v3
