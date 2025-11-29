class C1(object):

    def strongPasswordChecker(self, a1):
        """
        """
        v1 = 3
        if any(('a' <= c <= 'z' for v2 in a1)):
            v1 -= 1
        if any(('A' <= v2 <= 'Z' for v2 in a1)):
            v1 -= 1
        if any((v2.isdigit() for v2 in a1)):
            v1 -= 1
        v3 = 0
        v4, v5, v6 = (0, 0, 0)
        v7 = 2
        while v7 < len(a1):
            if a1[v7] == a1[v7 - 1] == a1[v7 - 2]:
                v8 = 2
                while v7 < len(a1) and a1[v7] == a1[v7 - 1]:
                    v8 += 1
                    v7 += 1
                v3 += v8 / 3
                if v8 % 3 == 0:
                    v4 += 1
                elif v8 % 3 == 1:
                    v5 += 1
                else:
                    v6 += 1
            else:
                v7 += 1
        if len(a1) < 6:
            return max(v1, 6 - len(a1))
        elif len(a1) <= 20:
            return max(v1, v3)
        else:
            v9 = len(a1) - 20
            v3 -= min(v9, v4 * 1) / 1
            v3 -= min(max(v9 - v4, 0), v5 * 2) / 2
            v3 -= min(max(v9 - v4 - 2 * v5, 0), v6 * 3) / 3
            return v9 + max(v1, v3)
