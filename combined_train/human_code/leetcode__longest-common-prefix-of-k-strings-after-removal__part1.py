class C1(object):

    def longestCommonPrefix(self, a1, a2):
        """
        """
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: a1[x])

        def longest_common_prefix(a1):
            v1 = [0] * len(a1)
            for v2 in range(len(a1) - (a1 - 1)):
                v3 = a1[v1[v2]]
                v4 = a1[v1[v2 + (a1 - 1)]]
                v5 = min(len(v3), len(v4))
                v1[v2] = next((j for v6 in range(v5) if v3[v6] != v4[v6]), v5)
            return v1
        v2 = longest_common_prefix(a2)
        v3 = [0] * len(a1)
        v3[0] = v2[0]
        for v4 in range(len(v3) - 1):
            v3[v4 + 1] = max(v3[v4], v2[v4 + 1])
        v5 = [0] * len(a1)
        v5[-1] = v2[-1]
        for v4 in reversed(range(len(v5) - 1)):
            v5[v4] = max(v5[v4 + 1], v2[v4])
        v6 = [0] * len(a1)
        v7 = max(longest_common_prefix(a2 + 1))
        for v4 in range(len(a1)):
            v8 = v1[v4]
            v9 = v3[v4 - a2] if v4 - a2 >= 0 else 0
            v10 = v5[v4 + 1] if v4 + 1 < len(a1) else 0
            v6[v8] = max(v7, v9, v10)
        return v6
