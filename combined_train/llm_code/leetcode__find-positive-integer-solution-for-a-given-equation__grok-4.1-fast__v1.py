class C1:

    def findSolution(self, a1, a2):
        v1 = []
        v2 = 1
        while a1.f(v2, 1) < a2:
            v2 += 1
        v3 = 1
        while a1.f(1, v3) < a2:
            v3 += 1
        for v4 in range(1, v2 + 1):
            v5, v6 = (1, v3)
            while v5 <= v6:
                v7 = (v5 + v6) // 2
                v8 = a1.f(v4, v7)
                if v8 == a2:
                    v1.append([v4, v7])
                    break
                elif v8 < a2:
                    v5 = v7 + 1
                else:
                    v6 = v7 - 1
        return v1
