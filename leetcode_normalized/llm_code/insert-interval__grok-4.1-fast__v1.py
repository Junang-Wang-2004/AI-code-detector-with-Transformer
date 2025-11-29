class C1:

    def insert(self, a1, a2):
        v1, v2 = (0, 0)
        v3 = len(a1)
        v4, v5 = a2
        while v1 < v3 and a1[v1][1] < v4:
            v1 += 1
        v2 = v1
        while v2 < v3 and a1[v2][0] <= v5:
            v4 = min(v4, a1[v2][0])
            v5 = max(v5, a1[v2][1])
            v2 += 1
        return a1[:v1] + [[v4, v5]] + a1[v2:]
