class C1:

    def intersect(self, a1, a2):
        if len(a1) > len(a2):
            a1, a2 = (a2, a1)
        v3 = {}
        for v4 in a1:
            if v4 not in v3:
                v3[v4] = 0
            v3[v4] += 1
        v5 = []
        for v4 in a2:
            if v4 in v3 and v3[v4] > 0:
                v5.append(v4)
                v3[v4] -= 1
        return v5
