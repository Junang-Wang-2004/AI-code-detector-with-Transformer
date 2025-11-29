class C1(object):

    def mincostTickets(self, a1, a2):
        """
        """
        v1 = [1, 7, 30]
        v2 = v1[-1]
        v3 = [float('inf') for v4 in range(v2)]
        v3[0] = 0
        v5 = [0, 0, 0]
        for v4 in range(1, len(a1) + 1):
            v3[v4 % v2] = float('inf')
            for v6 in range(len(v1)):
                while v4 - 1 < len(a1) and a1[v4 - 1] > a1[v5[v6]] + v1[v6] - 1:
                    v5[v6] += 1
                v3[v4 % v2] = min(v3[v4 % v2], v3[v5[v6] % v2] + a2[v6])
        return v3[len(a1) % v2]
