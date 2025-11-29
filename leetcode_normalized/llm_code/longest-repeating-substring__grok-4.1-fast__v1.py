class C1(object):

    def longestRepeatingSubstring(self, a1):

        def has_repeat(a1):
            if a1 == 0:
                return True
            v1 = len(a1)
            v2 = 10 ** 9 + 7
            v3 = 31
            v4 = 10 ** 9 + 9
            v5 = 37
            v6 = [1] * (a1 + 1)
            v7 = [1] * (a1 + 1)
            for v8 in range(1, a1 + 1):
                v6[v8] = v6[v8 - 1] * v3 % v2
                v7[v8] = v7[v8 - 1] * v5 % v4
            v9 = 0
            v10 = 0
            v11 = set()
            for v8 in range(a1):
                v12 = ord(a1[v8]) - ord('a') + 1
                v9 = (v9 * v3 + v12) % v2
                v10 = (v10 * v5 + v12) % v4
            v11.add((v9, v10))
            for v8 in range(a1, v1):
                v13 = ord(a1[v8 - a1]) - ord('a') + 1
                v14 = ord(a1[v8]) - ord('a') + 1
                v9 = (v9 - v13 * v6[a1 - 1] % v2 + v2) % v2
                v9 = (v9 * v3 + v14) % v2
                v10 = (v10 - v13 * v7[a1 - 1] % v4 + v4) % v4
                v10 = (v10 * v5 + v14) % v4
                v15 = (v9, v10)
                if v15 in v11:
                    return True
                v11.add(v15)
            return False
        v1, v2 = (0, len(a1))
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if has_repeat(v3):
                v1 = v3 + 1
            else:
                v2 = v3
        return v1 - 1
