import bisect

class C1:

    def shortestWay(self, a1, a2):
        v1 = len(a1)
        v2 = [[] for v3 in range(26)]
        for v4 in range(v1):
            v2[ord(a1[v4]) - ord('a')].append(v4)
        v5 = 1
        v6 = 0
        for v7 in a2:
            v8 = ord(v7) - ord('a')
            v9 = v2[v8]
            if not v9:
                return -1
            v10 = bisect.bisect_left(v9, v6)
            if v10 < len(v9):
                v6 = v9[v10] + 1
            else:
                v5 += 1
                v6 = v9[0] + 1
        return v5
