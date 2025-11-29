class C1:

    def longestCommonPrefix(self, a1):

        def pref_len(a1, a2):
            v1 = min(len(a1), len(a2))
            for v2 in range(v1):
                if a1[v2] != a2[v2]:
                    return v2
            return v1
        v1 = len(a1)
        if v1 < 2:
            return [0] * v1
        v2 = [pref_len(a1[j], a1[j + 1]) for v3 in range(v1 - 1)]
        v4 = [0]
        for v5 in v2:
            v4.append(max(v4[-1], v5))
        v6 = [0] * v1
        for v3 in range(v1 - 2, -1, -1):
            v6[v3] = max(v2[v3], v6[v3 + 1])
        v7 = [0] * v1
        for v8 in range(1, v1 - 1):
            v7[v8] = pref_len(a1[v8 - 1], a1[v8 + 1])
        v9 = []
        for v8 in range(v1):
            v10 = v4[v8 - 1] if v8 >= 1 else 0
            v11 = v6[v8 + 1] if v8 + 1 < v1 else 0
            v9.append(max(v10, v11, v7[v8]))
        return v9
