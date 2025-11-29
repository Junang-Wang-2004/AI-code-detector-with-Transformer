import bisect

class C1(object):

    def maxSubstringLength(self, a1):
        """
        """

        def check(a1, a2):
            for v1 in idxs:
                if not v1:
                    continue
                v2 = bisect.bisect_left(v1, a1)
                v3 = bisect.bisect_right(v1, a2) - 1
                if not (v3 - v2 + 1 == len(v1) or v3 - v2 + 1 == 0):
                    return False
            return True
        v1 = [[] for v2 in range(26)]
        for v3, v4 in enumerate(a1):
            v1[ord(v4) - ord('a')].append(v3)
        v5 = -1
        for v4 in v1:
            if not v4:
                continue
            v6 = v4[0]
            for v7 in v1:
                if not v7:
                    continue
                v8 = v7[-1]
                if v6 <= v8 and v8 - v6 + 1 != len(a1) and check(v6, v8):
                    v5 = max(v5, v8 - v6 + 1)
        return v5
