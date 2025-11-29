class C1(object):

    def longestDecomposition(self, a1):

        def segments_match(a1, a2, a3, a4):
            for v1 in range(a2):
                if a1[a3 + v1] != a1[a4 + v1]:
                    return False
            return True
        v1 = a1
        v2 = len(v1)
        v3 = 0
        v4 = 0
        v5 = v2 - 1
        v6 = 29
        v7 = 10 ** 9 + 7
        while v4 < v5:
            v8 = (v5 - v4 + 1) // 2
            v9 = 0
            v10 = 0
            v11 = 1
            v12 = False
            v13 = 0
            while v13 < v8:
                v13 += 1
                v14 = ord(v1[v4 + v13 - 1]) - ord('a')
                v9 = (v9 * v6 + v14) % v7
                v15 = ord(v1[v5 - v13 + 1]) - ord('a')
                v10 = (v15 * v11 + v10) % v7
                v11 = v11 * v6 % v7
                if v9 == v10 and segments_match(v1, v13, v4, v5 - v13 + 1):
                    v3 += 1
                    v4 += v13
                    v5 -= v13
                    v12 = True
                    break
            if not v12:
                break
        return v3
