class C1:

    def maximumGood(self, a1):
        v1 = len(a1)
        v2 = 0
        for v3 in range(1 << v1):
            v4 = True
            for v5 in range(v1):
                if v3 & 1 << v5 == 0:
                    continue
                for v6 in range(v1):
                    v7 = a1[v5][v6]
                    if v7 == 2:
                        continue
                    v8 = bool(v3 & 1 << v6)
                    if v8 != bool(v7):
                        v4 = False
                        break
                if not v4:
                    break
            if v4:
                v9 = 0
                v10 = v3
                while v10:
                    v9 += 1
                    v10 &= v10 - 1
                v2 = max(v2, v9)
        return v2
