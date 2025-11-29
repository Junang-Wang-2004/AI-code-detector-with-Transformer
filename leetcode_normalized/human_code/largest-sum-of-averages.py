class C1(object):

    def largestSumOfAverages(self, a1, a2):
        """
        """
        v1 = [a1[0]]
        for v2 in range(1, len(a1)):
            v1.append(a1[v2] + v1[-1])
        v3 = [[0] * len(a1) for v4 in range(2)]
        for v5 in range(1, a2 + 1):
            for v2 in range(v5 - 1, len(a1)):
                if v5 == 1:
                    v3[v5 % 2][v2] = float(v1[v2]) / (v2 + 1)
                else:
                    for v6 in range(v5 - 2, v2):
                        v3[v5 % 2][v2] = max(v3[v5 % 2][v2], v3[(v5 - 1) % 2][v6] + float(v1[v2] - v1[v6]) / (v2 - v6))
        return v3[a2 % 2][-1]
