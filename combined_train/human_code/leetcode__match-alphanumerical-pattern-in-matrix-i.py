class C1(object):

    def findPattern(self, a1, a2):
        """
        """

        def check(a1, a2):
            v1 = [-1] * 26
            v2 = [False] * 10
            for v3 in range(len(a2)):
                for v4 in range(len(a2[0])):
                    v5 = a1[a1 + v3][a2 + v4]
                    if a2[v3][v4].isdigit():
                        if int(a2[v3][v4]) != v5:
                            return False
                        continue
                    v6 = ord(a2[v3][v4]) - ord('a')
                    if v1[v6] == -1:
                        if v2[v5]:
                            return False
                        v2[v5] = True
                        v1[v6] = v5
                        continue
                    if v1[v6] != v5:
                        return False
            return True
        return next(([i, j] for v1 in range(len(a1) - len(a2) + 1) for v2 in range(len(a1[0]) - len(a2[0]) + 1) if check(v1, v2)), [-1, -1])
