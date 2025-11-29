class C1(object):

    def longestDecomposition(self, a1):
        """
        """

        def compare(a1, a2, a3, a4):
            for v1 in range(a2):
                if a1[a3 + v1] != a1[a4 + v1]:
                    return False
            return True
        v1 = 10 ** 9 + 7
        v2 = 26
        v3 = 0
        v4, v5, v6, v7 = (0, 0, 0, 1)
        for v8 in range(len(a1)):
            v4 = (v2 * v4 + (ord(a1[v8]) - ord('a'))) % v1
            v5 = (v7 * (ord(a1[-1 - v8]) - ord('a')) + v5) % v1
            v6 += 1
            v7 = v7 * v2 % v1
            if v4 == v5 and compare(a1, v6, v8 - v6 + 1, len(a1) - 1 - v8):
                v3 += 1
                v4, v5, v6, v7 = (0, 0, 0, 1)
        return v3
