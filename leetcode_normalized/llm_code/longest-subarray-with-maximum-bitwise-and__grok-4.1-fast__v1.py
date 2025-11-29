class C1(object):

    def longestSubarray(self, a1):
        if not a1:
            return 0
        v1 = 1
        v2 = a1[0]
        v3 = 1
        for v4 in a1[1:]:
            if v4 > v2:
                v2 = v4
                v3 = 1
            elif v4 == v2:
                v3 += 1
            else:
                v3 = 0
            v1 = max(v1, v3)
        return v1
