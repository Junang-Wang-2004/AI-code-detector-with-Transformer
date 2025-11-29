class C1:

    def balancedString(self, a1):
        v1 = len(a1)
        v2 = v1 // 4
        v3 = {}
        for v4 in a1:
            v3[v4] = v3.get(v4, 0) + 1
        v5 = {v4: 0 for v4 in v3}
        v6 = v1
        v7 = 0
        for v8 in range(v1):
            v5[a1[v8]] += 1
            while v7 <= v8:
                v9 = True
                for v4 in v3:
                    if v3[v4] - v5[v4] > v2:
                        v9 = False
                        break
                if v9:
                    v6 = min(v6, v8 - v7 + 1)
                    v5[a1[v7]] -= 1
                    v7 += 1
                else:
                    break
        return v6
