class C1(object):

    def findUnsortedSubarray(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = -1
        v3 = float('-inf')
        for v4 in range(v1):
            if a1[v4] < v3:
                v2 = v4
            v3 = max(v3, a1[v4])
        v5 = v1
        v6 = float('inf')
        for v4 in range(v1 - 1, -1, -1):
            if a1[v4] > v6:
                v5 = v4
            v6 = min(v6, a1[v4])
        return 0 if v5 > v2 else v2 - v5 + 1
