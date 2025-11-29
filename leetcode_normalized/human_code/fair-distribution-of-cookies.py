class C1(object):

    def distributeCookies(self, a1, a2):
        """
        """
        v1 = [0] * (1 << len(a1))
        for v2 in range(1 << len(a1)):
            v1[v2] = sum((a1[i] for v3 in range(len(a1)) if v2 & 1 << v3))
        v4 = [[float('inf')] * (1 << len(a1)) for v5 in range(2)]
        v4[0][0] = 0
        for v3 in range(a2):
            for v2 in range(1 << len(a1)):
                v6 = v2
                while v6:
                    v4[(v3 + 1) % 2][v2] = min(v4[(v3 + 1) % 2][v2], max(v1[v6], v4[v3 % 2][v2 ^ v6]))
                    v6 = v6 - 1 & v2
        return v4[a2 % 2][-1]
