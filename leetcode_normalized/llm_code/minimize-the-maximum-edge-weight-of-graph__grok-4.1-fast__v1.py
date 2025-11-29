class C1:

    def minMaxWeight(self, a1, a2, a3):
        if a1 == 1:
            return 0
        v1 = [{} for v2 in range(a1)]
        v3 = set()
        for v4, v5, v6 in a2:
            if v4 not in v1[v5] or v6 < v1[v5][v4]:
                v1[v5][v4] = v6
            v3.add(v6)
        if not v3:
            return -1
        v7 = sorted(v3)

        def reachable(a1):
            v1 = [False] * a1
            v1[0] = True
            v2 = [0]
            while v2:
                v3 = v2.pop()
                for v4, v5 in v1[v3].items():
                    if v5 <= a1 and (not v1[v4]):
                        v1[v4] = True
                        v2.append(v4)
            return all(v1)
        v8, v9 = (0, len(v7) - 1)
        while v8 <= v9:
            v10 = v8 + (v9 - v8) // 2
            if reachable(v7[v10]):
                v9 = v10 - 1
            else:
                v8 = v10 + 1
        return v7[v8] if v8 < len(v7) else -1
