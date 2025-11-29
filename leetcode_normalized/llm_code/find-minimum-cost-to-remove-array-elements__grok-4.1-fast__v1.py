class C1(object):

    def minCost(self, a1):
        v1 = {a1[0]: 0}
        v2 = 1
        while v2 < len(a1) - 1:
            v3 = {}
            v4, v5 = (a1[v2], a1[v2 + 1])
            for v6, v7 in v1.items():
                v8 = sorted([v4, v5, v6])
                v9 = v7 + v8[2]
                v3[v8[0]] = min(v3.get(v8[0], float('inf')), v9)
                v10 = v7 + v8[1]
                v3[v8[2]] = min(v3.get(v8[2], float('inf')), v10)
            v1 = v3
            v2 += 2
        v11 = a1[-1] if len(a1) % 2 == 0 else 0
        v12 = min((v7 + max(key_val, v11) for v13, v7 in v1.items()))
        return v12
