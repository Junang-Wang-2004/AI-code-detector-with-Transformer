class C1(object):

    def maxKilledEnemies(self, a1):
        """
        """
        v1 = 0
        if not a1 or not a1[0]:
            return v1
        v2 = [[0 for v3 in range(len(a1[0]))] for v3 in range(len(a1))]
        v4 = [[0 for v3 in range(len(a1[0]))] for v3 in range(len(a1))]
        for v5 in reversed(range(len(a1))):
            for v6 in reversed(range(len(a1[0]))):
                if a1[v5][v6] != 'W':
                    if v5 + 1 < len(a1):
                        v2[v5][v6] = v2[v5 + 1][v6]
                    if v6 + 1 < len(a1[0]):
                        v4[v5][v6] = v4[v5][v6 + 1]
                    if a1[v5][v6] == 'E':
                        v2[v5][v6] += 1
                        v4[v5][v6] += 1
        v7 = [0 for v3 in range(len(a1[0]))]
        for v5 in range(len(a1)):
            v8 = 0
            for v6 in range(len(a1[0])):
                if a1[v5][v6] == 'W':
                    v7[v6], v8 = (0, 0)
                elif a1[v5][v6] == 'E':
                    v7[v6] += 1
                    v8 += 1
                else:
                    v1 = max(v1, v8 + v7[v6] + v4[v5][v6] + v2[v5][v6])
        return v1
