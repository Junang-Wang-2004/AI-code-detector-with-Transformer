class C1(object):

    def getLengthOfOptimalCompression(self, a1, a2):
        """
        """

        def length(a1):
            v1 = 2 if a1 >= 2 else 1
            while a1 >= 10:
                v1 += 1
                a1 //= 10
            return v1
        v1 = [[len(a1)] * (a2 + 1) for v2 in range(len(a1) + 1)]
        v1[0][0] = 0
        for v3 in range(1, len(a1) + 1):
            for v4 in range(a2 + 1):
                if v3 - 1 >= 0 and v4 - 1 >= 0:
                    v1[v3][v4] = min(v1[v3][v4], v1[v3 - 1][v4 - 1])
                v5 = v6 = 0
                for v7 in range(v3, len(a1) + 1):
                    if a1[v3 - 1] == a1[v7 - 1]:
                        v5 += 1
                    else:
                        v6 += 1
                    if v4 + v6 <= a2:
                        v1[v7][v4 + v6] = min(v1[v7][v4 + v6], v1[v3 - 1][v4] + length(v5))
        return v1[len(a1)][a2]
