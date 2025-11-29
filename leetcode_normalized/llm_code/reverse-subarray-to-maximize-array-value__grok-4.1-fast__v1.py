class C1(object):

    def maxValueAfterReverse(self, a1):
        v1 = 0
        v2 = float('-inf')
        v3 = float('inf')
        v4 = 0
        v5, v6 = (a1[0], a1[-1])
        v7 = len(a1)
        for v8 in range(v7 - 1):
            v1 += abs(a1[v8] - a1[v8 + 1])
            v9 = min(a1[v8], a1[v8 + 1])
            v10 = max(a1[v8], a1[v8 + 1])
            v2 = max(v2, v9)
            v3 = min(v3, v10)
        for v8 in range(1, v7):
            v11 = abs(a1[v8 - 1] - a1[v8])
            v4 = max(v4, abs(v5 - a1[v8]) - v11)
            v4 = max(v4, abs(v6 - a1[v8 - 1]) - v11)
        v12 = 2 * (v2 - v3)
        return v1 + max(v4, v12)
