class C1(object):

    def ways(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0] * len(a1[0]) for v3 in range(len(a1))]
        for v4 in reversed(range(len(a1[0]))):
            v5 = 0
            for v6 in reversed(range(len(a1))):
                v5 += int(a1[v6][v4] == 'A')
                v2[v6][v4] = (v2[v6][v4 + 1] if v4 + 1 < len(a1[0]) else 0) + v5
        v7 = [[[0] * a2 for v3 in range(len(a1[0]))] for v3 in range(len(a1))]
        for v6 in reversed(range(len(a1))):
            for v4 in reversed(range(len(a1[0]))):
                v7[v6][v4][0] = 1
                for v8 in range(1, a2):
                    for v9 in range(v6 + 1, len(a1)):
                        if v2[v6][v4] == v2[v9][v4]:
                            continue
                        if v2[v9][v4] == 0:
                            break
                        v7[v6][v4][v8] = (v7[v6][v4][v8] + v7[v9][v4][v8 - 1]) % v1
                    for v9 in range(v4 + 1, len(a1[0])):
                        if v2[v6][v4] == v2[v6][v9]:
                            continue
                        if v2[v6][v9] == 0:
                            break
                        v7[v6][v4][v8] = (v7[v6][v4][v8] + v7[v6][v9][v8 - 1]) % v1
        return v7[0][0][a2 - 1]
