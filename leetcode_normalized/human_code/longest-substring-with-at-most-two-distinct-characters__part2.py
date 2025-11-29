from collections import Counter

class C1(object):

    def lengthOfLongestSubstringTwoDistinct(self, a1):
        """
        """
        v1 = Counter()
        v2, v3 = (0, 0)
        for v4, v5 in enumerate(a1):
            v1[v5] += 1
            while len(v1) > 2:
                v1[a1[v2]] -= 1
                if v1[a1[v2]] == 0:
                    del v1[a1[v2]]
                v2 += 1
            v3 = max(v3, v4 - v2 + 1)
        return v3
