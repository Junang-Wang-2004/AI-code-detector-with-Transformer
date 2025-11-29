class C1(object):

    def goodBinaryStrings(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = max(a3, a4) + 1
        v4 = [0] * v3
        v4[0] = 1
        for v5 in range(a2 + 1):
            if v5 >= a1:
                v2 = (v2 + v4[v5 % v3]) % v1
            if v5 + a3 <= a2:
                v4[(v5 + a3) % v3] = (v4[(v5 + a3) % v3] + v4[v5 % v3]) % v1
            if v5 + a4 <= a2:
                v4[(v5 + a4) % v3] = (v4[(v5 + a4) % v3] + v4[v5 % v3]) % v1
            v4[v5 % v3] = 0
        return v2
