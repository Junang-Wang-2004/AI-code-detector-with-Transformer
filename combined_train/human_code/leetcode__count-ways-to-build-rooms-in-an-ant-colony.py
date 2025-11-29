class C1(object):

    def waysToBuildRooms(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [1, 1]
        v3 = [0, 1]
        v4 = [1, 1]

        def nCr(a1, a2):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1

        def dfs(a1, a2):
            v1, v2 = (1, 0)
            for v3 in a1[a2]:
                v4, v5 = dfs(a1, v3)
                v2 += v5
                v1 = v1 * v4 % v1 * nCr(v2, v5) % v1
            return (v1, v2 + 1)
        v5 = [[] for v6 in range(len(a1))]
        for v7 in range(1, len(a1)):
            v5[a1[v7]].append(v7)
        return dfs(v5, 0)[0]
