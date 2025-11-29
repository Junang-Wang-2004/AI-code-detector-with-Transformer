class C1:

    def maxPalindromesAfterOperations(self, a1):
        v1 = sorted([len(word) for v2 in a1])
        v3 = [0] * 26
        v4 = ''.join(a1)
        for v5 in v4:
            v3[ord(v5) - 97] += 1
        v6 = 0
        for v7 in v3:
            v6 += v7 // 2
        v8 = v6
        for v9 in range(len(v1)):
            v10 = v1[v9] // 2
            if v8 < v10:
                return v9
            v8 -= v10
        return len(a1)
