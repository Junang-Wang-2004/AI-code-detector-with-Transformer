class C1(object):

    def maxOutput(self, a1, a2, a3):
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = max(a3)
        v6 = 10 ** 18

        def explore(a1, a2):
            nonlocal ans
            v1 = max(v1, a3[a1])
            v2 = -v6
            v3 = -v6
            for v4 in v1[a1]:
                if v4 == a2:
                    continue
                v5 = explore(v4, a1)
                v1 = max(v1, a3[a1] + v5)
                v1 = max(v1, a3[a1] + v2 + v5)
                v1 = max(v1, a3[a1] + v3 + v5)
                if v5 > v2:
                    v3 = v2
                    v2 = v5
                elif v5 > v3:
                    v3 = v5
            v6 = v2 if v2 > -v6 else -v6
            return a3[a1] + max(0, v6)
        explore(0, -1)
        return v5
