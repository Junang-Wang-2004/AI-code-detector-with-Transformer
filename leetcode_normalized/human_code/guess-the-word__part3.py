class C1(object):

    def findSecretWord(self, a1, a2):
        """
        """

        def solve(a1, a2):
            v1, v2 = (a2, None)
            for v3 in a2:
                v4 = [[] for v5 in range(7)]
                for v6 in a2:
                    if v6 != v3:
                        v4[a1[v3][v6]].append(v6)
                v7 = v4[0]
                if len(v7) < len(v1):
                    v1, v2 = (v7, v3)
            return v2
        v1 = [[sum((a == b for v2, v3 in zip(a1[i], a1[j]))) for v4 in range(len(a1))] for v5 in range(len(a1))]
        v6 = list(range(len(a1)))
        v7 = 0
        while v7 < 6:
            v8 = solve(v1, v6)
            v7 = a2.guess(a1[v8])
            v6 = [v4 for v4 in v6 if v1[v8][v4] == v7]
