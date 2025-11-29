class C1(object):

    def calculateMinimumHP(self, a1):
        v1 = 0
        for v2 in a1:
            for v3 in v2:
                if v3 < 0:
                    v1 += abs(v3)
        return self.binarySearch(a1, v1)

    def binarySearch(self, a1, a2):
        v1, v2 = (1, a2 + 1)
        v3 = 0
        while v1 < v2:
            v4 = v1 + (v2 - v1) / 2
            if self.DP(a1, v4):
                v2 = v4
            else:
                v1 = v4 + 1
        return v1

    def DP(self, a1, a2):
        v1 = [0 for v2 in a1[0]]
        v1[0] = a2 + a1[0][0]
        for v3 in range(1, len(v1)):
            if v1[v3 - 1] > 0:
                v1[v3] = max(v1[v3 - 1] + a1[0][v3], 0)
        for v4 in range(1, len(a1)):
            if v1[0] > 0:
                v1[0] = max(v1[0] + a1[v4][0], 0)
            else:
                v1[0] = 0
            for v3 in range(1, len(v1)):
                v5 = 0
                if v1[v3 - 1] > 0:
                    v5 = max(v1[v3 - 1] + a1[v4][v3], v5)
                if v1[v3] > 0:
                    v5 = max(v1[v3] + a1[v4][v3], v5)
                v1[v3] = v5
        return v1[-1] > 0
