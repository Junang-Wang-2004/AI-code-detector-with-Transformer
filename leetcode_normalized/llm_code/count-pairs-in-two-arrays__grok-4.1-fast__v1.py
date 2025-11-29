class C1:

    def countPairs(self, a1, a2):
        v1 = [a - b for v2, v3 in zip(a1, a2)]
        v1.sort()
        v4 = len(v1)
        v5 = 0
        v6, v7 = (0, v4 - 1)
        while v6 < v7:
            if v1[v6] + v1[v7] > 0:
                v5 += v7 - v6
                v7 -= 1
            else:
                v6 += 1
        return v5
