class C1(object):

    def numberOfArrays(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = len(str(a2))
        v3 = [0] * (v2 + 1)
        v3[len(a1) % len(v3)] = 1
        for v4 in reversed(range(len(a1))):
            v3[v4 % len(v3)] = 0
            if a1[v4] == '0':
                continue
            v5 = 0
            for v6 in range(v4, min(v4 + v2, len(a1))):
                v5 = 10 * v5 + int(a1[v6])
                if v5 > a2:
                    break
                v3[v4 % len(v3)] = (v3[v4 % len(v3)] + v3[(v6 + 1) % len(v3)]) % v1
        return v3[0]
