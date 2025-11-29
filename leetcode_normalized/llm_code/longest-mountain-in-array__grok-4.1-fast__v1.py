class C1:

    def longestMountain(self, a1):
        v1 = 0
        v2 = len(a1)
        v3 = 0
        while v3 < v2:
            v4 = v3
            while v3 < v2 - 1 and a1[v3 + 1] > a1[v3]:
                v3 += 1
            v5 = v3
            v6 = v3
            while v3 < v2 - 1 and a1[v3 + 1] < a1[v3]:
                v3 += 1
            v7 = v3
            if v5 > v4 and v7 > v5:
                v1 = max(v1, v7 - v4 + 1)
            if v5 == v4 and v7 == v4:
                v3 += 1
        return v1
