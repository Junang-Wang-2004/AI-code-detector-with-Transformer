class C1:

    def waysToBuildRooms(self, a1):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [[] for v4 in range(v2)]
        for v5 in range(1, v2):
            v3[a1[v5]].append(v5)
        v6 = [1] * (v2 + 1)
        for v5 in range(1, v2 + 1):
            v6[v5] = v6[v5 - 1] * v5 % v1
        v7 = [0] * (v2 + 1)
        v7[v2] = pow(v6[v2], v1 - 2, v1)
        for v5 in range(v2 - 1, -1, -1):
            v7[v5] = v7[v5 + 1] * (v5 + 1) % v1

        def comb(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v6[a1] * v7[a2] % v1 * v7[a1 - a2] % v1

        def traverse(a1):
            v1 = 1
            v2 = 0
            v3 = 1
            for v4 in v3[a1]:
                v5, v6 = traverse(v4)
                v1 = v1 * v5 % v1
                v7 = comb(v2 + v6, v6)
                v1 = v1 * v7 % v1
                v2 += v6
                v3 += v6
            return (v1, v3)
        return traverse(0)[0]
