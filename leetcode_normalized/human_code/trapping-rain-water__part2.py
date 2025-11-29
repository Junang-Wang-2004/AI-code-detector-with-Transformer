class C1(object):

    def trap(self, a1):
        v1 = 0
        v2 = 0
        for v3 in range(len(a1)):
            if a1[v2] < a1[v3]:
                v2 = v3
        v4 = 0
        for v3 in range(v2):
            if a1[v4] < a1[v3]:
                v4 = v3
            v1 += a1[v4] - a1[v3]
        v4 = len(a1) - 1
        for v3 in reversed(range(v2, len(a1))):
            if a1[v4] < a1[v3]:
                v4 = v3
            v1 += a1[v4] - a1[v3]
        return v1
