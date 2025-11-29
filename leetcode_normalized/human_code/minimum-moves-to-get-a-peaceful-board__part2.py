class C1(object):

    def minMoves(self, a1):
        """
        """

        def count(a1):
            v1 = [0] * len(a1)
            for v2 in a1:
                v1[v2] += 1
            v3 = v4 = 0
            for v5 in range(len(a1)):
                v4 += v1[v5] - 1
                v3 += abs(v4)
            return v3
        return sum((count(arr) for v1 in zip(*a1)))
