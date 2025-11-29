class C1:

    def findSmallestRegion(self, a1, a2, a3):
        v1 = {}
        for v2 in a1:
            v3 = v2[0]
            for v4 in v2[1:]:
                v1[v4] = v3

        def climb_to_root(a1):
            v1 = []
            v2 = a1
            while v2 in v1:
                v1.append(v2)
                v2 = v1[v2]
            v1.append(v2)
            return v1[::-1]
        v5 = climb_to_root(a2)
        v6 = climb_to_root(a3)
        v7 = 0
        v8 = min(len(v5), len(v6))
        while v7 < v8 and v5[v7] == v6[v7]:
            v7 += 1
        return v5[v7 - 1]
