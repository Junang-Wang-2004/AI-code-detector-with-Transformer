class C1(object):

    def numTilePossibilities(self, a1):
        """
        """

        def backtracking(a1):
            v1 = 0
            for v2, v3 in a1.items():
                if not v3:
                    continue
                a1[v2] -= 1
                v1 += 1 + backtracking(a1)
                a1[v2] += 1
            return v1
        return backtracking(collections.Counter(a1))
