class C1(object):

    def findLengthOfShortestSubarray(self, a1):
        """
        """
        v1 = 0
        for v2 in range(1, len(a1)):
            if a1[v2 - 1] <= a1[v2]:
                continue
            v3 = len(a1) - 1
            while v3 > v2 and (v3 == len(a1) - 1 or a1[v3] <= a1[v3 + 1]) and (a1[v2 - 1] <= a1[v3]):
                v3 -= 1
            v1 = v3 - v2 + 1
            break
        for v3 in reversed(range(len(a1) - 1)):
            if a1[v3] <= a1[v3 + 1]:
                continue
            v2 = 0
            while v2 < v3 and (v2 == 0 or a1[v2 - 1] <= a1[v2]) and (a1[v2] <= a1[v3 + 1]):
                v2 += 1
            v1 = min(v1, v3 - v2 + 1)
            break
        return v1
