class C1(object):

    def minimumCost(self, a1):
        """
        """

        def nearest_palindromic(a1):
            v1 = str(a1)
            v2 = len(v1)
            v3 = {10 ** v2 + 1, 10 ** (v2 - 1) - 1}
            v4 = int(v1[:(v2 + 1) / 2])
            for v5 in map(str, (v4 - 1, v4, v4 + 1)):
                v3.add(int(v5 + [v5, v5[:-1]][v2 % 2][::-1]))
            return v3
        a1.sort()
        v1 = a1[len(a1) // 2]
        if len(a1) % 2 == 0:
            v1 = (v1 + a1[len(a1) // 2 - 1]) // 2
        return min((sum((abs(x - p) for v2 in a1)) for v3 in nearest_palindromic(v1)))
