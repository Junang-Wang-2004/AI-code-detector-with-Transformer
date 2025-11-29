class C1(object):

    def distinctEchoSubstrings(self, a1):
        """
        """

        def compare(a1, a2, a3, a4):
            for v1 in range(a2):
                if a1[a3 + v1] != a1[a4 + v1]:
                    return False
            return True
        v1 = 10 ** 9 + 7
        v2 = 27
        v3 = set()
        for v4 in range(len(a1)):
            v5, v6, v7 = (0, 0, 1)
            for v8 in range(1, min(v4 + 2, len(a1) - v4)):
                v5 = (v2 * v5 + (ord(a1[v4 - v8 + 1]) - ord('a') + 1)) % v1
                v6 = (v7 * (ord(a1[v4 + v8]) - ord('a') + 1) + v6) % v1
                if v5 == v6 and compare(a1, v8, v4 - v8 + 1, v4 + 1):
                    v3.add(a1[v4 + 1:v4 + 1 + v8])
                v7 = v7 * v2 % v1
        return len(v3)
