class C1:

    def maximumLengthSubstring(self, a1):
        v1 = [0] * 26
        v2 = 0
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            v6 = ord(a1[v5]) - ord('a')
            if v1[v6] == 2:
                v2 += 1
            v1[v6] += 1
            while v2 > 0 and v3 <= v5:
                v7 = ord(a1[v3]) - ord('a')
                v1[v7] -= 1
                if v1[v7] == 2:
                    v2 -= 1
                v3 += 1
            v4 = max(v4, v5 - v3 + 1)
        return v4
