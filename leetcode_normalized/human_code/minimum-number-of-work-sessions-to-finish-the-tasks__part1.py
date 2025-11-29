class C1(object):

    def minSessions(self, a1, a2):
        """
        """
        v1 = [float('inf') for v2 in range(1 << len(a1))]
        v1[0] = 0
        for v3 in range(len(v1) - 1):
            v4 = 1
            for v5 in a1:
                v6 = v3 | v4
                v4 <<= 1
                if v6 == v3:
                    continue
                if v1[v3] % a2 + v5 > a2:
                    v5 += a2 - v1[v3] % a2
                v1[v6] = min(v1[v6], v1[v3] + v5)
        return (v1[-1] + a2 - 1) // a2
