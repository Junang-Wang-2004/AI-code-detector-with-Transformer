class C1:

    def longestPalindrome(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = 0
        v4 = False
        for v2 in v1:
            v5 = v2[::-1]
            if v2 == v5:
                v3 += v1[v2] // 2 * 4
                if v1[v2] % 2:
                    v4 = True
        v6 = set()
        for v2 in v1:
            if v2 in v6 or v2 == v2[::-1]:
                continue
            v5 = v2[::-1]
            if v5 in v1:
                v7 = min(v1[v2], v1[v5])
                v3 += v7 * 4
                v6.add(v2)
                v6.add(v5)
        if v4:
            v3 += 2
        return v3
