class C1(object):

    def minMoves(self, a1):
        """
        """

        def count(a1):
            v1 = [0] * len(a1)
            for v2 in a1:
                v1[v2] += 1
            return sum((abs(i - v2) for v3, v2 in enumerate((v2 for v2, v1 in enumerate(v1) for v4 in range(v1)))))
        return sum((count(arr) for v1 in zip(*a1)))
