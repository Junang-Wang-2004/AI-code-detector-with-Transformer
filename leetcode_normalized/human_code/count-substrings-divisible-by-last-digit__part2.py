class C1(object):

    def countSubstrings(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] == '4':
                v1 += 1
                if v2 - 1 >= 0 and int(a1[v2 - 1:v2 + 1]) % 4 == 0:
                    v1 += v2
        for v2 in range(len(a1)):
            if a1[v2] == '8':
                v1 += 1
                if v2 - 1 >= 0 and int(a1[v2 - 1:v2 + 1]) % 8 == 0:
                    v1 += 1
                if v2 - 2 >= 0 and int(a1[v2 - 2:v2 + 1]) % 8 == 0:
                    v1 += v2 - 1
        for v3 in range(1, 9 + 1):
            if v3 in (4, 8):
                continue
            v4 = 1
            v5 = 0
            v6 = [0] * v3
            v7 = 0
            for v2 in range(len(a1)):
                v5 = (v5 + v4 * (ord(a1[~v2]) - ord('0'))) % v3
                v7 += v6[v5]
                if a1[~v2] == str(v3):
                    v7 += v3 != 8
                    v6[v5] += 1
                v4 = v4 * 10 % v3
            v1 += v7
        return v1
