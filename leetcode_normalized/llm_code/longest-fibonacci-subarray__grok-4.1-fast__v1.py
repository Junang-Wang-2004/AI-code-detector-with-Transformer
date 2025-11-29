class C1(object):

    def longestSubarray(self, a1):
        v1 = len(a1)
        if v1 <= 2:
            return v1
        v2 = 2
        v3 = 2
        for v4 in range(2, v1):
            if a1[v4] == a1[v4 - 2] + a1[v4 - 1]:
                v3 += 1
                v2 = max(v2, v3)
            else:
                v3 = 2
        return v2
