class C1:

    def smallestDistancePair(self, a1, a2):
        a1.sort()
        v1, v2 = (0, a1[-1] - a1[0])
        while v1 < v2:
            v3 = (v1 + v2) // 2
            v4 = 0
            v5 = 0
            v6 = len(a1)
            for v7 in range(v6):
                while v5 < v6 and a1[v5] <= a1[v7] + v3:
                    v5 += 1
                v4 += v5 - v7 - 1
            if v4 >= a2:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
