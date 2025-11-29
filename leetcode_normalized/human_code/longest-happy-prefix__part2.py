class C1(object):

    def longestPrefix(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 26

        def check(a1, a2):
            for v1 in range(a1):
                if a2[v1] != a2[len(a2) - a1 + v1]:
                    return False
            return True
        v3, v4, v5, v6 = (0, 0, 0, 1)
        for v7 in range(len(a1) - 1):
            v4 = (v4 * v2 + (ord(a1[v7]) - ord('a'))) % v1
            v5 = (v5 + (ord(a1[len(a1) - (v7 + 1)]) - ord('a')) * v6) % v1
            v6 = v6 * v2 % v1
            if v4 == v5:
                v3 = v7 + 1
        return a1[:v3]
