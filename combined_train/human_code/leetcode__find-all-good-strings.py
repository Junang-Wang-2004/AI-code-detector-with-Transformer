class C1(object):

    def findGoodStrings(self, a1, a2, a3, a4):
        """
        """
        v1 = 10 ** 9 + 7

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 != -1 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1
        v2 = getPrefix(a4)
        v3 = [[[[0] * len(a4) for v4 in range(2)] for v4 in range(2)] for v4 in range(2)]
        v3[0][0][0][0] = 1
        for v5 in range(a1):
            v3[(v5 + 1) % 2] = [[[0] * len(a4) for v4 in range(2)] for v4 in range(2)]
            for v6 in range(2):
                for v7 in range(2):
                    v8 = 'a' if v6 else a2[v5]
                    v9 = 'z' if v7 else a3[v5]
                    for v10 in range(len(a4)):
                        if not v3[v5 % 2][v6][v7][v10]:
                            continue
                        for v11 in range(ord(v8) - ord('a'), ord(v9) - ord('a') + 1):
                            v11 = chr(v11 + ord('a'))
                            v12 = v10 - 1
                            while v12 != -1 and a4[v12 + 1] != v11:
                                v12 = v2[v12]
                            if a4[v12 + 1] == v11:
                                v12 += 1
                            if v12 + 1 == len(a4):
                                continue
                            v3[(v5 + 1) % 2][v6 or a2[v5] != v11][v7 or a3[v5] != v11][v12 + 1] = (v3[(v5 + 1) % 2][v6 or a2[v5] != v11][v7 or a3[v5] != v11][v12 + 1] + v3[v5 % 2][v6][v7][v10]) % v1
        v13 = 0
        for v6 in range(2):
            for v7 in range(2):
                for v10 in range(len(a4)):
                    v13 = (v13 + v3[a1 % 2][v6][v7][v10]) % v1
        return v13
