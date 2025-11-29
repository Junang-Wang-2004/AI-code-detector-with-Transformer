import bisect

class C1(object):

    def minDifference(self, a1, a2):
        """
        """
        v1 = float('inf')
        v2 = [[] for v3 in range(max(a1) + 1)]
        for v4, v5 in enumerate(a1):
            v2[v5].append(v4)
        v6 = []
        for v7, v8 in a2:
            v9, v10 = (v1, -1)
            for v5 in range(len(v2)):
                v4 = bisect.bisect_left(v2[v5], v7)
                if not (v4 < len(v2[v5]) and v2[v5][v4] <= v8):
                    continue
                if v10 != -1:
                    v9 = min(v9, v5 - v10)
                v10 = v5
            v6.append(v9 if v9 != v1 else -1)
        return v6
