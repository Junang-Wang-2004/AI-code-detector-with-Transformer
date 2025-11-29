class C1(object):

    def maxSubstringLength(self, a1, a2):
        """
        """

        def erase_overlap_intervals(a1):
            a1.sort(key=lambda interval: interval[1])
            v1, v2 = (0, float('-inf'))
            for v3, v4 in a1:
                if v3 <= v2:
                    v1 += 1
                else:
                    v2 = v4
            return v1
        v1 = [0] * 26
        v2, v3 = ([-1] * 26, [-1] * 26)
        for v4, v5 in enumerate(a1):
            v1[ord(v5) - ord('a')] += 1
            if v2[ord(v5) - ord('a')] == -1:
                v2[ord(v5) - ord('a')] = v4
            v3[ord(v5) - ord('a')] = v4
        v6 = []
        for v4 in range(len(a1)):
            if v4 != v2[ord(a1[v4]) - ord('a')]:
                continue
            v7 = v4 + 1
            v8 = v3[ord(a1[v4]) - ord('a')]
            while v7 <= v8 and v2[ord(a1[v7]) - ord('a')] >= v4:
                v8 = max(v8, v3[ord(a1[v7]) - ord('a')])
                v7 += 1
            if v7 == v8 + 1 and (v4 != 0 or v8 != len(a1) - 1):
                v6.append((v4, v8))
        return len(v6) - erase_overlap_intervals(v6) >= a2
