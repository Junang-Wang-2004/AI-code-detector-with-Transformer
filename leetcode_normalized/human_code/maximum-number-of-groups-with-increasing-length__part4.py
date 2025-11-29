class C1(object):

    def maxIncreasingGroups(self, a1):
        """
        """

        def check(a1):
            return all(((i + 1) * i // 2 <= prefix[len(a1) - (a1 - i)] for v1 in range(1, a1 + 1)))
        a1.sort()
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3, v4 = (1, len(a1))
        while v3 <= v4:
            v5 = v3 + (v4 - v3) // 2
            if not check(v5):
                v4 = v5 - 1
            else:
                v3 = v5 + 1
        return v4
