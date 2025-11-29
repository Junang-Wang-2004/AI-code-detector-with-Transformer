class C1(object):

    def minValidStrings(self, a1, a2):
        """
        """
        v1, v2 = (10 ** 9 + 7, 131)
        v3 = [1]
        for v4 in range(len(a2)):
            v3.append(v3[-1] * v2 % v1)
        v5 = set()
        for v6 in a1:
            v7 = 0
            for v8 in v6:
                v7 = (v7 * v2 + (ord(v8) - ord('a') + 1)) % v1
                v5.add(v7)
        v9 = [0] * (len(a2) + 1)
        v10 = v7 = 0
        for v11 in range(len(a2)):
            v7 = (v7 * v2 + (ord(a2[v11]) - ord('a') + 1)) % v1
            while v11 - v10 + 1 >= 1 and v7 not in v5:
                v7 = (v7 - (ord(a2[v10]) - ord('a') + 1) * v3[v11 - v10 + 1 - 1]) % v1
                v10 += 1
            if v11 - v10 + 1 == 0:
                return -1
            v9[v11 + 1] = v9[v11 - (v11 - v10 + 1) + 1] + 1
        return v9[-1]
