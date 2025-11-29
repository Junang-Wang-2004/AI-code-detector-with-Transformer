class C1(object):

    def minTrioDegree(self, a1, a2):
        """
        """
        v1 = [set() for v2 in range(a1 + 1)]
        v3 = [0] * (a1 + 1)
        for v4, v5 in a2:
            v1[min(v4, v5)].add(max(v4, v5))
            v3[v4] += 1
            v3[v5] += 1
        v6 = float('inf')
        for v4 in range(1, a1 + 1):
            for v5 in v1[v4]:
                for v7 in v1[v4]:
                    if v5 < v7 and v7 in v1[v5]:
                        v6 = min(v6, v3[v4] + v3[v5] + v3[v7] - 6)
        return v6 if v6 != float('inf') else -1
