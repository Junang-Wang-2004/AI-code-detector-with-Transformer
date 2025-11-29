class C1(object):

    def findGoodStrings(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7
        v2 = len(a4)
        v3 = [0] * v2
        v4 = 0
        for v5 in range(1, v2):
            while v4 > 0 and a4[v5] != a4[v4]:
                v4 = v3[v4 - 1]
            if a4[v5] == a4[v4]:
                v4 += 1
            v3[v5] = v4
        v6 = [[0] * 26 for v7 in range(v2 + 1)]
        for v8 in range(v2 + 1):
            for v9 in range(26):
                v10 = chr(ord('a') + v9)
                if v8 < v2 and a4[v8] == v10:
                    v6[v8][v9] = v8 + 1
                else:
                    v11 = v3[v8 - 1] if v8 > 0 else 0
                    v6[v8][v9] = v6[v11][v9]
        v12 = {}

        def count(a1, a2, a3, a4):
            if a1 == a1:
                return 1
            v1 = (a1, a2, a3, a4)
            if v1 in v12:
                return v12[v1]
            v2 = 0
            v3 = ord(a2[a1]) - ord('a') if a2 else 0
            v4 = ord(a3[a1]) - ord('a') if a3 else 25
            for v5 in range(v3, v4 + 1):
                v6 = a2 and v5 == v3
                v7 = a3 and v5 == v4
                v8 = v6[a4][v5]
                if v8 == v2:
                    continue
                v2 = (v2 + count(a1 + 1, v6, v7, v8)) % v1
            v12[v1] = v2
            return v2
        return count(0, True, True, 0)
