import bisect

class C1:

    def minimumMountainRemovals(self, a1):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = []
        for v4 in range(v1):
            v5 = bisect.bisect_left(v3, a1[v4])
            v2[v4] = v5 + 1
            if v5 == len(v3):
                v3.append(a1[v4])
            else:
                v3[v5] = a1[v4]
        v6 = [0] * v1
        v3 = []
        for v4 in range(v1 - 1, -1, -1):
            v5 = bisect.bisect_left(v3, a1[v4])
            v6[v4] = v5 + 1
            if v5 == len(v3):
                v3.append(a1[v4])
            else:
                v3[v5] = a1[v4]
        v7 = 1
        for v4 in range(1, v1 - 1):
            v7 = max(v7, v2[v4] + v6[v4] - 1)
        return v1 - v7
