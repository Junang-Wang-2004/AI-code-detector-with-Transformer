class C1(object):

    def minSwap(self, a1, a2):
        v1 = 0
        v2 = 1
        for v3 in range(1, len(a1)):
            v4 = float('inf')
            v5 = float('inf')
            if a1[v3 - 1] < a1[v3] and a2[v3 - 1] < a2[v3]:
                v4 = min(v4, v1)
                v5 = min(v5, v2 + 1)
            if a1[v3 - 1] < a2[v3] and a2[v3 - 1] < a1[v3]:
                v4 = min(v4, v2)
                v5 = min(v5, v1 + 1)
            v1 = v4
            v2 = v5
        return min(v1, v2)
