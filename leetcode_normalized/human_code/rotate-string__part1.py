class C1(object):

    def rotateString(self, a1, a2):
        """
        """

        def check(a1):
            return all((a1[(i + a1) % len(a1)] == c for v1, v2 in enumerate(a2)))
        if len(a1) != len(a2):
            return False
        v1, v2 = (10 ** 9 + 7, 113)
        v3 = pow(v2, v1 - 2, v1)
        v4, v5 = (0, 1)
        for v6 in a2:
            v4 += v5 * ord(v6)
            v4 %= v1
            v5 = v5 * v2 % v1
        v7, v5 = (0, 1)
        for v8 in range(len(a2)):
            v7 += v5 * ord(a1[v8 % len(a1)])
            v7 %= v1
            v5 = v5 * v2 % v1
        if v7 == v4 and check(0):
            return True
        v5 = v5 * v3 % v1
        for v8 in range(len(a2), 2 * len(a1)):
            v7 = (v7 - ord(a1[(v8 - len(a2)) % len(a1)])) * v3
            v7 += v5 * ord(a1[v8 % len(a1)])
            v7 %= v1
            if v7 == v4 and check(v8 - len(a2) + 1):
                return True
        return False
