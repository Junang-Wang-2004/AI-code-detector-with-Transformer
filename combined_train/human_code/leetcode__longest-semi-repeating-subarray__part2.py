import collections

class C1(object):

    def longestSubarray(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = v3 = v4 = 0
        for v5 in range(len(a1)):
            v1[a1[v5]] += 1
            if v1[a1[v5]] == 2:
                v4 += 1
            while v4 > a2:
                if v1[a1[v3]] == 2:
                    v4 -= 1
                v1[a1[v3]] -= 1
                if not v1[a1[v3]]:
                    del v1[a1[v3]]
                v3 += 1
            v2 = max(v2, v5 - v3 + 1)
        return v2
