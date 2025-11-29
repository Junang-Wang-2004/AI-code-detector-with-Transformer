class C1(object):

    def countServers(self, a1, a2, a3, a4):
        """
        """
        a2.sort(key=lambda x: a3[1])
        v1 = [0] * len(a4)
        v2 = [0] * a1
        v3 = v4 = v5 = 0
        for v6, v7 in sorted(((v6, v7) for v7, v6 in enumerate(a4))):
            while v5 < len(a2) and a2[v5][1] <= v6:
                if v2[a2[v5][0] - 1] == 0:
                    v3 += 1
                v2[a2[v5][0] - 1] += 1
                v5 += 1
            while v4 < v5 and a2[v4][1] < v6 - a3:
                v2[a2[v4][0] - 1] -= 1
                if v2[a2[v4][0] - 1] == 0:
                    v3 -= 1
                v4 += 1
            v1[v7] = a1 - v3
        return v1
