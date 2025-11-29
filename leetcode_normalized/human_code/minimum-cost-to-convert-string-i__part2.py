class C1(object):

    def minimumCost(self, a1, a2, a3, a4, a5):
        """
        """
        v1 = float('inf')

        def floydWarshall(a1):
            for v1 in range(len(a1)):
                for v2 in range(len(a1)):
                    if a1[v2][v1] == v1:
                        continue
                    for v3 in range(len(a1[v2])):
                        if a1[v1][v3] == v1:
                            continue
                        a1[v2][v3] = min(a1[v2][v3], a1[v2][v1] + a1[v1][v3])
        v2 = [[0 if u == v else v1 for v3 in range(26)] for v4 in range(26)]
        for v5 in range(len(a3)):
            v4, v3 = (ord(a3[v5]) - ord('a'), ord(a4[v5]) - ord('a'))
            v2[v4][v3] = min(v2[v4][v3], a5[v5])
        floydWarshall(v2)
        v6 = sum((v2[ord(a1[v5]) - ord('a')][ord(a2[v5]) - ord('a')] for v5 in range(len(a1))))
        return v6 if v6 != v1 else -1
