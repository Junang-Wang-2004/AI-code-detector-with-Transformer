class C1(object):

    def subStrHash(self, a1, a2, a3, a4, a5):
        """
        """
        v1, v2 = (0, -1)
        v3 = pow(a2, a4 - 1, a3)
        for v4 in reversed(range(len(a1))):
            if v4 + a4 < len(a1):
                v1 = (v1 - (ord(a1[v4 + a4]) - ord('a') + 1) * v3) % a3
            v1 = (v1 * a2 + (ord(a1[v4]) - ord('a') + 1)) % a3
            if v1 == a5:
                v2 = v4
        return a1[v2:v2 + a4]
