class C1(object):

    def shortestPalindrome(self, a1):
        """
        """

        def preProcess(a1):
            if not a1:
                return ['^', '$']
            v1 = ['^']
            for v2 in a1:
                v1 += ['#', v2]
            v1 += ['#', '$']
            return v1
        v1 = preProcess(a1)
        v2 = [0] * len(v1)
        v3, v4 = (0, 0)
        for v5 in range(1, len(v1) - 1):
            v6 = 2 * v3 - v5
            if v4 > v5:
                v2[v5] = min(v4 - v5, v2[v6])
            else:
                v2[v5] = 0
            while v1[v5 + 1 + v2[v5]] == v1[v5 - 1 - v2[v5]]:
                v2[v5] += 1
            if v5 + v2[v5] > v4:
                v3, v4 = (v5, v5 + v2[v5])
        v7 = 0
        for v5 in range(1, len(v1) - 1):
            if v5 - v2[v5] == 1:
                v7 = v2[v5]
        return a1[len(a1) - 1:v7 - 1:-1] + a1
