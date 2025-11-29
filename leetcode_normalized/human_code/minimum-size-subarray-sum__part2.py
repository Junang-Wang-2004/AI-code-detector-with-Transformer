class C1(object):

    def minSubArrayLen(self, a1, a2):
        v1 = float('inf')
        v2 = [n for v3 in a2]
        for v4 in range(len(v2) - 1):
            v2[v4 + 1] += v2[v4]
        for v4 in range(len(v2)):
            v5 = self.binarySearch(lambda x, y: x <= y, v2, v4, len(v2), v2[v4] - a2[v4] + a1)
            if v5 < len(v2):
                v1 = min(v1, v5 - v4 + 1)
        return v1 if v1 != float('inf') else 0

    def binarySearch(self, a1, a2, a3, a4, a5):
        while a3 < a4:
            v1 = a3 + (a4 - a3) / 2
            if a1(a5, a2[v1]):
                a4 = v1
            else:
                a3 = v1 + 1
        return a3
