class C1(object):

    def sortMatrix(self, a1):
        if not a1 or not a1[0]:
            return a1
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = 1 - v2
        v4 = v1 - 1
        v5 = {d: [] for v6 in range(v3, v4 + 1)}
        for v7 in range(v1):
            for v8 in range(v2):
                v5[v7 - v8].append(a1[v7][v8])
        for v6 in range(v3, v4 + 1):
            if v6 < 0:
                v5[v6].sort(reverse=True)
            else:
                v5[v6].sort()
        for v7 in range(v1):
            for v8 in range(v2):
                a1[v7][v8] = v5[v7 - v8].pop()
        return a1
