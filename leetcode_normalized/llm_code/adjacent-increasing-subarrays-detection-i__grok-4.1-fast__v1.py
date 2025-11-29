class C1(object):

    def hasIncreasingSubarrays(self, a1, a2):
        if not a1:
            return False
        v1 = 0
        v2 = 0
        v3 = 0
        v4 = len(a1)
        while v3 < v4:
            v5 = v3
            while v3 + 1 < v4 and a1[v3] < a1[v3 + 1]:
                v3 += 1
            v6 = v3 - v5 + 1
            v1 = max(v1, v6 // 2)
            if v2 > 0:
                v1 = max(v1, min(v2, v6))
            v2 = v6
            v3 += 1
        return v1 >= a2
