class C1(object):

    def networkBecomesIdle(self, a1, a2):
        """
        """
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0]
        v6 = [False] * len(a2)
        v6[0] = True
        v7 = 1
        v8 = 0
        while v5:
            v9 = []
            for v3 in v5:
                for v4 in v1[v3]:
                    if v6[v4]:
                        continue
                    v6[v4] = True
                    v9.append(v4)
                    v8 = max(v8, (v7 * 2 - 1) // a2[v4] * a2[v4] + v7 * 2)
            v5 = v9
            v7 += 1
        return 1 + v8
