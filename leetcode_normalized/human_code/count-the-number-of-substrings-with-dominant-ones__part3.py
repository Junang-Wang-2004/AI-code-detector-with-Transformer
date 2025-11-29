class C1(object):

    def numberOfSubstrings(self, a1):
        """
        """
        v1 = 0
        for v2 in range(int((-1 + (1 + 4 * len(a1)) ** 0.5) / 2) + 1):
            v3 = [0] * 2
            v4 = v5 = 0
            for v6 in range(len(a1)):
                v3[a1[v6] == '1'] += 1
                while v3[0] == v2 + 1:
                    v3[a1[v4] == '1'] -= 1
                    v4 += 1
                if not (v3[0] == v2 and v3[1] >= v2 ** 2):
                    continue
                for v5 in range(max(v5, v4), v6):
                    if a1[v5] == '0':
                        break
                else:
                    v5 = v6
                v1 += min(v5 - v4 + 1, v3[1] - v2 ** 2 + 1)
        return v1
