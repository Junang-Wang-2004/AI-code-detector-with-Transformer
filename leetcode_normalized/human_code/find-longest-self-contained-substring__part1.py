import bisect

class C1(object):

    def maxSubstringLength(self, a1):
        """
        """

        def check(a1, a2):
            for v1 in idxs:
                if not v1 or v1[-1] < a1 or v1[0] > a2 or (a1 <= v1[0] and v1[-1] <= a2):
                    continue
                v2 = bisect.bisect_left(v1, a1)
                if v2 != len(v1) and v1[v2] <= a2:
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
                if v6 <= v8 and v5 < v8 - v6 + 1 != len(a1) and check(v6, v8):
                    v5 = v8 - v6 + 1
        return v5
