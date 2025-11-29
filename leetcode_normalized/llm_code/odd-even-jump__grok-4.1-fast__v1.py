class C1:

    def oddEvenJumps(self, a1):
        v1 = len(a1)
        v2 = [None] * v1
        v3 = []
        for v4 in range(v1 - 1, -1, -1):
            while v3 and a1[v3[-1]] < a1[v4]:
                v3.pop()
            if v3:
                v2[v4] = v3[-1]
            v3.append(v4)
        v5 = [v1] * v1
        v3 = []
        for v4 in range(v1 - 1, -1, -1):
            while v3 and a1[v3[-1]] <= a1[v4]:
                v3.pop()
            if v3:
                v5[v4] = v3[-1]
            v3.append(v4)
        v6 = [None] * v1
        for v4 in range(v1):
            v7 = v5[v4] - 1
            if v7 > v4:
                v6[v4] = v7
        v8 = [False] * v1
        v9 = [False] * v1
        v8[v1 - 1] = True
        v9[v1 - 1] = True
        for v4 in range(v1 - 2, -1, -1):
            if v2[v4] is not None:
                v8[v4] = v9[v2[v4]]
            if v6[v4] is not None:
                v9[v4] = v8[v6[v4]]
        return sum(v8)
