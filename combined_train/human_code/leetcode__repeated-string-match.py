class C1(object):

    def repeatedStringMatch(self, a1, a2):
        """
        """

        def check(a1):
            return all((a1[(i + a1) % len(a1)] == c for v1, v2 in enumerate(a2)))
        v1, v2 = (10 ** 9 + 7, 113)
        v3 = pow(v2, v1 - 2, v1)
        v4 = (len(a2) + len(a1) - 1) // len(a1)
        v5, v6 = (0, 1)
        for v7 in a2:
            v5 += v6 * ord(v7)
            v5 %= v1
            v6 = v6 * v2 % v1
        v8, v6 = (0, 1)
        for v9 in range(len(a2)):
            v8 += v6 * ord(a1[v9 % len(a1)])
            v8 %= v1
            v6 = v6 * v2 % v1
        if v8 == v5 and check(0):
            return v4
        v6 = v6 * v3 % v1
        for v9 in range(len(a2), (v4 + 1) * len(a1)):
            v8 = (v8 - ord(a1[(v9 - len(a2)) % len(a1)])) * v3
            v8 += v6 * ord(a1[v9 % len(a1)])
            v8 %= v1
            if v8 == v5 and check(v9 - len(a2) + 1):
                return v4 if v9 < v4 * len(a1) else v4 + 1
        return -1
