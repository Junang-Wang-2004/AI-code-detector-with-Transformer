class C1(object):

    def minFlips(self, a1):
        """
        """
        v1 = float('inf')
        v2 = v3 = 0
        for v4 in range(2 * len(a1) - 1 if len(a1) % 2 else len(a1)):
            if v4 >= len(a1):
                v2 -= int(a1[v4 % len(a1)]) ^ (v4 - len(a1)) % 2 ^ 0
                v3 -= int(a1[v4 % len(a1)]) ^ (v4 - len(a1)) % 2 ^ 1
            v2 += int(a1[v4 % len(a1)]) ^ v4 % 2 ^ 0
            v3 += int(a1[v4 % len(a1)]) ^ v4 % 2 ^ 1
            if v4 >= len(a1) - 1:
                v1 = min(v1, v2, v3)
        return v1
