class C1:

    def pourWater(self, a1, a2, a3):
        v1 = len(a1)
        for v2 in range(a2):
            v3 = a3
            v4 = a1[a3]
            v5 = a3
            while v5 > 0 and a1[v5 - 1] <= v4:
                v5 -= 1
                if a1[v5] < v4:
                    v4 = a1[v5]
                    v3 = v5
            if v3 != a3:
                a1[v3] += 1
                continue
            v4 = a1[a3]
            v5 = a3
            v3 = a3
            while v5 + 1 < v1 and a1[v5 + 1] <= v4:
                v5 += 1
                if a1[v5] < v4:
                    v4 = a1[v5]
                    v3 = v5
            a1[v3] += 1
        return a1
