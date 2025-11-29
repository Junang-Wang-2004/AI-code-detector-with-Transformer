class C1:

    def threeSumClosest(self, a1, a2):
        v1 = sorted(a1)
        v2 = 0
        v3 = float('inf')
        v4 = len(v1)
        for v5 in range(v4 - 2):
            if v5 > 0 and v1[v5] == v1[v5 - 1]:
                continue
            v6 = v5 + 1
            v7 = v4 - 1
            while v6 < v7:
                v8 = v1[v5] + v1[v6] + v1[v7]
                if v8 == a2:
                    return a2
                v9 = abs(v8 - a2)
                if v9 < v3:
                    v3 = v9
                    v2 = v8
                if v8 < a2:
                    v6 += 1
                else:
                    v7 -= 1
        return v2
