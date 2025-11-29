class C1:

    def maxNumOfSubstrings(self, a1):
        v1 = len(a1)
        v2 = [v1] * 26
        v3 = [-1] * 26
        for v4, v5 in enumerate(a1):
            v6 = ord(v5) - ord('a')
            v2[v6] = min(v2[v6], v4)
            v3[v6] = max(v3[v6], v4)

        def compute_end(a1):
            v1 = v3[ord(a1[a1]) - ord('a')]
            v2 = a1
            while v2 <= v1:
                v3 = ord(a1[v2]) - ord('a')
                if v2[v3] < a1:
                    return -1
                v1 = max(v1, v3[v3])
                v2 += 1
            return v1
        v7 = []
        for v4 in range(26):
            v8 = v2[v4]
            if v8 < v1:
                v9 = compute_end(v8)
                if v9 != -1:
                    v7.append((v9, v8))
        v7.sort()
        v10 = []
        v11 = -1
        for v9, v8 in v7:
            if v8 > v11:
                v10.append(a1[v8:v9 + 1])
                v11 = v9
        return v10
