class C1(object):

    def mostProfitablePath(self, a1, a2, a3):
        v1 = len(a1) + 1
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [float('inf')] * v1

        def compute_bob_time(a1, a2):
            if a1 == a2:
                v6[a1] = 0
                return 0
            v1 = float('inf')
            for v2 in v2[a1]:
                if v2 == a2:
                    continue
                v3 = compute_bob_time(v2, a1)
                v1 = min(v1, v3 + 1)
            v6[a1] = v1
            return v1
        compute_bob_time(0, -1)

        def compute_profit(a1, a2, a3):
            v1 = v6[a1]
            v2 = a3[a1]
            if a3 == v1:
                v2 //= 2
            elif a3 > v1:
                v2 = 0
            v3 = 0
            for v4 in v2[a1]:
                if v4 == a2:
                    continue
                v3 = max(v3, compute_profit(v4, a1, a3 + 1))
            return v2 + v3
        return compute_profit(0, -1, 0)
