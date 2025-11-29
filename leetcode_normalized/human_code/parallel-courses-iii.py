class C1(object):

    def minimumTime(self, a1, a2, a3):
        """
        """
        v1 = [[] for v2 in range(a1)]
        v3 = [0] * a1
        for v4, v5 in a2:
            v1[v4 - 1].append(v5 - 1)
            v3[v5 - 1] += 1
        v6 = [u for v7 in range(a1) if not v3[v7]]
        v8 = [a3[v7] if not v3[v7] else 0 for v7 in range(a1)]
        while v6:
            v9 = []
            for v7 in v6:
                for v10 in v1[v7]:
                    v8[v10] = max(v8[v10], v8[v7] + a3[v10])
                    v3[v10] -= 1
                    if not v3[v10]:
                        v9.append(v10)
            v6 = v9
        return max(v8)
