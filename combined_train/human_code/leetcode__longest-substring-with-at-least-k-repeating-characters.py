class C1(object):

    def longestSubstring(self, a1, a2):
        """
        """

        def longestSubstringHelper(a1, a2, a3, a4):
            v1 = [0] * 26
            for v2 in range(a3, a4):
                v1[ord(a1[v2]) - ord('a')] += 1
            v3 = 0
            v2 = a3
            while v2 < a4:
                while v2 < a4 and v1[ord(a1[v2]) - ord('a')] < a2:
                    v2 += 1
                v4 = v2
                while v4 < a4 and v1[ord(a1[v4]) - ord('a')] >= a2:
                    v4 += 1
                if v2 == a3 and v4 == a4:
                    return a4 - a3
                v3 = max(v3, longestSubstringHelper(a1, a2, v2, v4))
                v2 = v4
            return v3
        return longestSubstringHelper(a1, a2, 0, len(a1))
