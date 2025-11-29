class C1:

    def minCost(self, a1, a2):
        v1 = len(a1)
        v2 = float('inf')
        v3 = [v2] * v1
        v3[0] = 0
        v4 = []
        v5 = []

        def update(a1, a2, a3, a4, a5, a6):
            while a1 and a6(a3[a1[-1]], a3[a2]):
                v1 = a1.pop()
                a4[a2] = min(a4[a2], a4[v1] + a5[a2])
        for v6 in range(v1):
            update(v4, v6, a1, v3, a2, lambda x, y: x <= y)
            v4.append(v6)
            update(v5, v6, a1, v3, a2, lambda x, y: x > y)
            v5.append(v6)
        return v3[-1]
